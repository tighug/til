# db-migrate

db-migrate とは、**Node.js の DB マイグレーションの一つ**です。

- [node-db-migrate](https://github.com/db-migrate/node-db-migrate)

## Installation

=== "NPM"

    ```bash
    npm install -S db-migrate
    ```

=== "Yarn"

    ```bash
    yarn add db-migrate
    ```

## Command

| command            | description                                        |
| ------------------ | -------------------------------------------------- |
| `up`               | `migrations`ディレクトリの migrate を行う。        |
| `down`             | `migrations`ディレクトリの drop を行う。           |
| `reset`            | リセットする。                                     |
| `create [name]`    | `migrations`ディレクトリにテンプレートを作成する。 |
| `db:create [name]` | 現在の構成で、データベースを作成する。             |
| `db:drop [name]`   | 現在の構成で、データベースを削除する。             |

### SQL ファイルを使用する

`create`時に`--sqlfile`オプションを付けると、SQL ファイルと、それらをロードする JS コードを自動生成してくれる。

```bash
db-migrate create add-people --sql-file
```

これにより、以下の 3 つのファイルが作成される。

```bash
./migrations/20111219120000-add-people.js
./migrations/sqls/20111219120000-add-people-up.sql
./migrations/sqls/20111219120000-add-people-down.sql
```

また、`database.json`に設定しておくことで、デフォルトで`--sql-file`オプションが有効になる。

```json
// database.json
{
  "sql-file": true
}
```

### SQL API

```js
createTable（tableName, columnSpec, callback）
dropTable（tableName, options, callback）
addColumn（tableName, columnName, columnSpec, callback）
removeColumn（tableName, columnName, callback）
renameColumn（tableName、oldColumnName、newColumnName、コールバック）
```

## Usage

### 1. database.json を用意する

```json
{
  "development": {
    "host": { "ENV": "DB_HOST" },
    "user": { "ENV": "DB_USER" },
    "password": { "ENV": "DB_PASSWORD" },
    "database": { "ENV": "DB_NAME" },
    "driver": "mysql",
    "multipleStatements": true
  }
}
```

### 2. `create`でテンプレートを作成する

```bash
yarn run db-migrate create [table name]
```

### 3. `migrations`ディレクトリ内のファイルを適宜編集する

### 4.（まだない場合）`db:create`でデータベースを作成する

```bash
yarn run db-migrate db:create [DB name]
```

### 5. `up`で migrate する

```bash
yarn run db-migrate up
```
