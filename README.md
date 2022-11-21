# flask_user-crud

flaskで作成したUserのCRUD APIです

3層アーキテクチャになるように実装しています

## Getting Started

docker環境立ち上げ

```
make up
```

makeのコマンド一覧については ```make help```で確認できます

## Direcotry

```
|--config             # 設定回り
|  |--db
|  |  |--conn.py      # dbの接続情報
|  |  |--db.py        # dbの情報
|  |  |--session.py   # dbのセッション情報
|--main.py            # main関数、最初に実行されるファイル
|--model              # ビジネスモデル
|  |--user.py
|--presentation       # web関係のロジック
|  |--controller      # APIのコントローラー
|  |  |--user.py
|  |--router          # APIのルーターの管理
|  |  |--router.py    # flaskのappのオブジェクトを管理、またすべてのルーターを集約する
|  |  |--user.py      # userのルーターを管理
|--repository         # DBへの永続化を責務とする
|  |--user.py
|--service            # アプリのビジネスロジック
|  |--user.py
|--utils              # 便利ツールなど
|  |--error           # errorオブジェクト
|  |  |--error.py
```

## API

## GET /
healthチェック

ex:  http://localhost:8000

response
```json
{
    "health": "good!"
}
```


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

## POST  /user
userの登録をする

ex: http://localhost:8000/user

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
