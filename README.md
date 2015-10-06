# InfoMarquee
Simple TV like marquee with two lines with different priorities and different duration time of each message.

## What's behind
Application is running in Docker container environment. Backend is written in Python Flask with Redis as database. 
Frontend is using jQuery framework.

## How to run
1. Clone github repo:
`$ git clone https://github.com/witalisoft/infomarquee.git`
2. Build container image:
`$ sudo docker build -t infomarquee:latest -f Dockerfile .`
3. Run container:
`$ sudo docker run -d -p 8000:8000 infomarquee:latest`
4. Application is available under:
`http://localhost:8000/static/index.html`

## Usage
InfoMarquee expose simple REST API. 

| command       | description                  | example                                                                                |
| ------------- |:-----------------------------| :--------------------------------------------------------------------------------------|
| `GET /get`    | get current list of marquee  | `$ curl http://localhost:8000/get`                                                     |
| `POST /set`   | set new marquee with duration (sec) of each one             | `$ curl -d @input.json -H "Content-Type: application/json" http://localhost:8000/set`  |

example of input.json:

```json
{ "newalert": 
    { "high": [
        { "text": "your new high alert text", "duration": 60 },
        { "text": "your new high alert text2", "duration": 60 }
       ],
       "normal": [
        { "text": "your normal alert text", "duration": 50 },
        { "text": "your normal alert text2", "duration": 50 },
        { "text": "your normal alert text3", "duration": 50 },
        { "text": "your normal alert text4", "duration": 50 }
       ]
    }
}
```




