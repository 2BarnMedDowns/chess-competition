import Chessnut as cn
import datetime as dt
import re

DEFAULT_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


class Board(object):
    def __init__(self, fen, timeout, increment):
        self.game = cn.Game(fen, True)
        self._invalid_move = False
        self._time_white = timeout
        self._time_black = timeout
        self._increment = increment
        self._history = []
        self._timestamp = dt.datetime.now()


    def captures(self):
        pieces = {}
        for piece in "rnbqkbnrpppppppp":
            Piece = piece.upper()
            if not piece in pieces:
                pieces[piece] = 0
            if not Piece in pieces:
                pieces[Piece] = 0

            pieces[piece] += 1
            pieces[Piece] += 1

        i = 0
        fen = self.fen
        while fen[i] != ' ':
            c = fen[i]
            if c in pieces:
                pieces[c] -= 1
            i += 1

        captures = []
        for piece, num in pieces.iteritems():
            if num > 0:
                for i in xrange(num):
                    captures.append(piece)

        return captures

    @property
    def fen(self):
        return self.game.get_fen()

    def __str__(self):
        return self.fen

    def move(self, coordinate_notation):
        before = self.fen

        try:
            self.game.apply_move(coordinate_notation)
        except cn.game.InvalidMove as e:
            self._invalid_move = True
            return False

        except Exception as e:
            raise e

        after = self.fen



        return True

    @property
    def history(self):
        return self.game.move_history

    @property
    def status(self):
        if self._invalid_move:
            return "illegal-move"

        statuses = ['normal', 'check', 'checkmate', 'stalemate']
        return statuses[self.game.status]
