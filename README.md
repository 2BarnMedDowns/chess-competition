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
**Request**
```
GET /board HTTP/1.1
Accept: application/json
```

**Response**
```
HTTP/1.1 200 OK
Content-Type: application/json

{
	"fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 
	"captures": [],
	"status": "ok", 
	"history": []
}
```

### Reset board
**Request**
```
PUT /board HTTP/1.1
Accept: application/json
Content-Type: application/json

{"reset": true}
```

**Response**
```
HTTP/1.1 200 OK
Content-Type: application/json

{
	"fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 
	"captures": [],
	"status": "ok", 
	"history": []
}
```

### Reset board with different parameters
**Request**
```
PUT /board HTTP/1.1
Accept: application/json
Content-Type: application/json

{
	"reset": true,
	"board": {
		"fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
		"time": 600,
		"increment": 30
	}
}
```

**Response**
```
HTTP/1.1 200 OK
Content-Type: application/json

{
	"fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 
	"captures": [],
	"status": "ok", 
	"history": []
}
```


### Make move
**Request**
```
PUT /board HTTP/1.1
Accept: application/json
Content-Type: application/json

{"move": "e2e4"}
```

**Response**
```
HTTP/1.1 200 OK
Content-Type: application/json

{
	"fen": "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",
	"captures": [],
	"status": "ok", 
	"history": ["e2e4"]
}
```

