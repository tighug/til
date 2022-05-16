# Restful API

Restful API とは、**REST と呼ばれる設計原則に従った API**です。

- [RESTful API 設計における HTTP ステータスコードの指針 | Qiita](https://qiita.com/uenosy/items/ba9dbc70781bddc4a491)
- [PUT か POST か PATCH か？ | Qiita](https://qiita.com/suin/items/d17bdfc8dba086d36115)
- [HTTP メソッド(CRUD)についてまとめた | Qiita](https://qiita.com/r_fukuma/items/a9e8d18467fe3e04068e)

## REST

REST：Representational State Transfer

1. アドレス指定可能な URI で公開されていること
2. インターフェース（**HTTP メソッド = CRUD**）の統一がされていること
3. **ステートレス**であること
4. 処理結果が**HTTP ステータスコード**で通知されること

## CRUD

CRUD：Create, Read, Update, Delete

HTTP メソッドでは以下の 4 つに該当します。

- **GET**：取得
- **POST**：作成
- **PUT**：更新
- **DELETE**：削除

## Stateless

ステートレスとは、サーバー側が状態を持たないということです。[ここ](http://yohei-y.blogspot.com/2007/10/blog-post.html)が非常に参考になります。

## HTTP Status Code

### GET

成功

- `200 OK`

### POST

成功

- `201 Created`
  - 作成したリソースの URI を示す`Location`ヘッダを付けておく

失敗

- `409 Conflict`
  - 作成しようとしたリソースが既にある場合

### PUT

成功

- `204 No Content`
  - 更新の場合
- `201 Created`
  - 新規作成の場合
  - 作成したリソースの URI を示す`Location`ヘッダを付けておく

失敗

- `409 Conflict`
  - 作成しようとしたリソースが既にある場合
  - 更新しようとしたリソースがロック中の場合

### PATCH

成功

- `200 OK`
  - パッチしたリソースを返却する場合
- `204 No Content`
  - パッチしたリソースを返却しない場合

失敗

- `409 Conflict`
  - 更新しようとしたリソースがロック中の場合

### DELETE

成功

- `204 No Content`

失敗

- `409 Conflict`
  - 更新しようとしたリソースがロック中の場合

### 共通

失敗

- `4xx`系
  - 通知することでクライアント側が反応できるもの。
  - `400 Bad Request`
    - データ形式が間違っている場合（JSON のパースエラー等）
  - `401 Unauthorized`
    - 何らかの認証が必要な場合
    - つまり、`Authorization`ヘッダが必要な場合
  - `402 Payment Required`
    - 支払いが必要な場合
  - `404 Not Found`
    - 存在しない場合
    - 存在することを隠したい（Forbidden）場合
  - `405 Method Not Allowed`
    - リソースに指定されたメソッドが用意されていない場合
  - `406 Not Acceptable`
    - `Accept ｀ヘッダとマッチしない場合
- `5xx`系
  - 通知してもクライアント側が反応できないもの。
  - `500 Internal Server Error`
    - サーバーが原因のエラーにより処理が続行できない場合
  - `503 Service Unavailable`
    - 一時的にサービス提供ができない場合（メンテナンス等）
