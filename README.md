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
GET / HTTP/1.1
Accept: application/json
```

**Response**
```
200 OK
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
PUT / HTTP/1.1
Accept: application/json
Content-Type: application/json

{"reset": true}
```

**Response**
```
200 OK
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
PUT / HTTP/1.1
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
200 OK
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
PUT / HTTP/1.1
Accept: application/json
Content-Type: application/json

{"move": "e2e4"}
```

**Response**
```
200 OK
Content-Type: application/json

{
	"fen": "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",
	"captures": [],
	"status": "ok", 
	"history": ["e2e4"]
}
```

