# hello kimura

## API

## GET  /user/:id
指定したuser id のuser を取得するAPI

ex: http://localhost:8000/user/1

response
```json
{
    "age": 12,
    "id": 1,
    "name": "doer"
}
```

## GET  /user/all
すべての user を取得するAPI

ex: http://localhost:8000/user/all

response
```json
{
    "users": [
        {
            "age": 12,
            "id": 1,
            "name": "doer"
        },
        {
            "age": 30,
            "id": 3,
            "name": "doshisha"
        }
    ]
}
```

## GET  /user/all
すべての user を取得するAPI

ex: http://localhost:8000/user/all
request body
```json
{
    "name":"hoge",
    "age":20
}
```

response
```json
{
    "age": 20,
    "id": null,
    "name": "hoge"
}
```
