Prerequisites
-------------
```
pip install flask
pip install chessnut
```

Run server
----------
`FLASK_APP=server.py FLASK_DEBUG=1 python -m flask run`
or alternatively
`./server.py`


API
-------

### Get board
```
GET / HTTP/1.1
Accept: application/json
```

### Reset board
```
PUT / HTTP/1.1
Accept: application/json
Content-Type: application/json

{"reset": true}
```


### Make move
```
PUT / HTTP/1.1
Accept: application/json
Content-Type: application/json

{"move": "e2e4"}
```
