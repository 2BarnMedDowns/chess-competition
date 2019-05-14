#!/usr/bin/env python
#coding=utf8
import re
import chess
import flask
import traceback as tb
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import MethodNotAllowed
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import UnsupportedMediaType
from werkzeug.exceptions import InternalServerError

app = flask.Flask(__name__)
api_handlers = {}
board = None


def api_handler(url, method):
    """Convenience decorator for flask routes"""
    method = method.upper()

    if not method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        raise Exception("Unknown method: ``{}''".format(method))

    def decorate(handler_func):
        def endpoint(*args, **kwargs):
            # Get flask's request context
            from flask import request

            accept_mimetype = request.accept_mimetypes.best_match(['application/json'])
            if accept_mimetype != "application/json":
                # Client asked for something other than JSON, we do not support that
                raise UnsupportedMediaType("Unsupported response format")

            if request.content_length > 0 and request.content_type != "application/json":
                # Client sent us something other than JSON
                app.logger.warn("Unknown request format: ``{}''".format(request.content_type))
                raise BadRequest("Unknown request format")

            req_data = request.get_json()
            if not req_data is None and not isinstance(req_data, dict):
                raise BadRequest("Invalid request format")

            headers = {}
            try:
                resp_data = handler_func(req_data, headers, *args, **kwargs)

            except HTTPException as e:
                app.logger.debug(tb.format_exc(e))
                raise e

            except Exception as e:
                app.logger.debug(tb.format_exc(e))
                raise InternalServerError(e)

            if resp_data is None:
                response = flask.make_response((None, headers.get('status', 200), headers))

            else:
                response = flask.Response(
                        response=flask.json.dumps(resp_data),
                        status=headers.get('status', 200),
                        headers=headers,
                        mimetype="application/json",
                        content_type="application/json"
                        )

            return response


        if handler_func:
            ep = handler_func.__name__ + "_" + method
            app.add_url_rule(url, ep, endpoint, methods=[method])


    return decorate


def board_info():
    global board
    if board is None:
        return {'board': None}

    fen = board.fen
    history = board.history

    return {'board': {
        'fen': fen,
        'status': "ok",
        'history': board.history,
        'captures': board.captures()
        }}


def reset_game(**board_data):
    global board
    fen = board_data.get('fen', chess.DEFAULT_FEN)
    timeout = board_data.get('time', -1)
    increment = board_data.get('increment', 0)

    try:
        board = chess.Board(fen, timeout, increment)
        app.logger.info("Resetting board: {}".format(board.fen))
    except Exception as e:
        app.logger.debug(e)
        board = None
        raise BadRequest("Invalid FEN string")


@api_handler('/board', 'GET')
def list_games(request_data, request_headers):
    return board_info()


@api_handler('/board', 'PUT')
def move_piece(request_data, headers):
    global board
    if 'reset' in request_data:
        if request_data['reset'] == True:
            reset_game(**request_data.get('board', {}))

    elif 'move' in request_data:
        board.move(request_data['move'])

    else:
        raise BadRequest()

    return board_info()


if __name__ == '__main__':
    app.run(use_debugger=True, use_reloader=True, debug=app.debug, host="0.0.0.0", port=5000)

