# dotenv

`dotenv`とは、**`.env` ファイルから `process.env` へ環境変数をロードするモジュール**です。
`.env`ファイルに書いた設定を環境変数として簡単に読み込めます。

## Installation

=== "NPM"

    ```bash
    npm install -S dotenv
    ```

=== "Yarn"

    ```bash
    yarn add dotenv
    ```

## Usage

### `.env`ファイルの作成

#### 1. `.env`ファイルを作成

```txt
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=database
DB_USERNAME=user
DB_PASSWORD=password
```

#### 2. `.env`を`.gitignore`に追加する

リモートリポジトリにプッシュするのは、セキュリティ的に良くない。

#### 3. `.env.template`を作成する

フォーマットは`git`で管理したいため。

```txt
DB_HOST=
DB_PORT=
DB_DATABASE=
DB_USERNAME=
DB_PASSWORD=
```

### 設定した環境変数を呼び出す

`processs.env`を環境変数の前に付けることで呼び出せる。

```ts
import dotenv from "dotenv";

detenv.config(); // 呼び出す前に記述する

cnosole.log(process.env.DB_HOST);
```
