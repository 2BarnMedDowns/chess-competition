#!/usr/bin/env python
import requests

port = 5000
url = "http://127.0.0.1:{}".format(port)


def move(board_url, move):
    r = requests.put(board_url, json={'move': move})
    assert r.status_code == 200
    info = r.json()
    assert 'board' in info
    return info['board']


if __name__ == '__main__':
    #r = requests.put(url, json={'reset': True, 'board': {'fen': "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"}})
    r = requests.put(url, json={'reset': True})
    assert r.status_code == 200
    info = r.json()
    assert 'board' in info
    board = info['board']
    print board

    move1 = move(url, "e2e4")
    assert "e2e4" in move1['history']
    print move1

