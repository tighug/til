# Sequelize

Sequelize とは、**Promise ベースの Node.js ORM の一つ**です。[npm trends](https://www.npmtrends.com/db-migrate-vs-sequelize)を見るに、`db-migrate`よりも人気そうです。

- [Manual \| Sequelize](https://sequelize.org/master/index.html)

## Installation

=== "NPM"

    ```bash
    npm install -S sequelize

    # CLI
    npm install -g sequelize-cli

    # One of the following:
    npm install -S pg pg-hstore # Postgres
    npm install -S mysql2
    npm install -S mariadb
    npm install -S sqlite3
    npm install -S tedious # Microsoft SQL Server
    ```

=== "Yarn"

    ```bash
    yarn add sequelize

    # CLI
    yarn global add sequelize-cli

    # One of the following:
    yarn add pg pg-hstore # Postgres
    yarn add mysql2
    yarn add mariadb
    yarn add sqlite3
    yarn add tedious # Microsoft SQL Server
    ```

## Setup

```js
const Sequelize = require("sequelize");

const sequelize = new Sequelize("database", "username", "password", {
  host: "localhost",
  dialect: "mysql",
  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000,
  },
});
```

### 接続テスト

```js
sequelize
  .authenticate()
  .then(() => {
    console.log("Connection has been established successfully.");
  })
  .catch((err) => {
    console.error("Unable to connect to the database:", err);
  });
```

### モデリング

```js
const User = sequelize.define(
  "user",
  {
    // attributes
    firstName: {
      type: Sequelize.STRING,
      allowNull: false,
    },
    lastName: {
      type: Sequelize.STRING,
      // allowNull defaults to true
    },
  },
  {
    // options
  }
);
```

## CLI

### 手順

まず、設定ファイル`.sequelizerc`を作成する。

```js
// .sequelizerc
const path = require("path");

module.exports = {
  config: path.resolve("config", "database.js"),
  "models-path": path.resolve("db", "models"),
  "seeders-path": path.resolve("db", "seeders"),
  "migrations-path": path.resolve("db", "migrations"),
};
```

`init`コマンドで、設定ファイルに従って以下のフォルダ/ファイルが生成される。

```bash
sequelize init
```

- `config/database.js`：データベースとの接続方法を CLI に指示する構成ファイル
- `db/models/index.js`：プロジェクトのすべてのモデル
- `db/migrations/`：すべての移行ファイル
- `db/seeders/`：すべてのシードファイル

生成された`config/database.js`を自分の設定に書き換える。
（以下の例は`dotenv`を利用したもの）

```js
// config/database.js
import dotenv from "dotenv";

dotenv.config();

module.exports = {
  development: {
    username: process.env.MYSQL_USER || process.env.DB_USER,
    password: process.env.MYSQL_PASSWORD || process.env.DB_PASSWORD,
    database: process.env.MYSQL_DATABASE || process.env.DB_DATABASE,
    host: process.env.MYSQL_HOST || process.env.DB_HOST,
    dialect: "mysql",
  },
};
```

`db:create`コマンドで、設定ファイルに指定したデータベースを作成する。

```bash
sequelize db:create
```

```bash
sequelize db:create # dbを作成
sequelize db:drop   # dbを落とす
sequelize db:migrate  # migrate実行
sequelize db:migrate:undo:all # 実行されたmigrateを全て取り消し
sequelize db:seed:all         # 設定されていたseedファイルをmigrate
seqeulize db:seed:undo:all    # seedファイルのmigrateを全て取り消し
```
