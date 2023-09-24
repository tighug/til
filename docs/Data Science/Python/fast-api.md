# FastAPI

FastAPI は、Python の Web フレームワークのひとつです。

## インストール

```bash
poetry add fastapi
```

!!! tip

    本番環境で使用する際には、[Uvicorn](./uvicorn.md)の併用を推奨します。

## クイックスタート

以下で`http://localhost:8000`にライブサーバーが起動します。また、`http://localhost:8000/docs`に Swagger 製の API ドキュメントサーバーが起動します。

```py title="main.py"
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

```bash title="bash"
uvicorn main:app --reload
```

## 参考文献

-   [FastAPI](https://fastapi.tiangolo.com/ja/)
