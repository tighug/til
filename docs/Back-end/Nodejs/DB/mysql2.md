# mysql2

## インストール

=== "npm"

    ```bash
    npm install -S mysql2
    ```

=== "yarn"

    ```bash
    yarn add mysql2
    ```

## 使い方

### インポート

```ts
import mysql from "mysql2";

// or, promise wrapper
import mysql from "mysql2/promise";
```

### 接続

```ts
const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  database: "test",
});
```

### クエリ

```ts
connection.query(
  "SELECT * FROM `table` WHERE `name` = ? AND `age` > ?",
  ["Page", 45],
  function (err, results) {
    console.log(results);
  }
);
```

```ts
connection.execute(
  "SELECT * FROM `table` WHERE `name` = ? AND `age` > ?",
  ["Rick C-137", 53],
  function (err, results, fields) {
    console.log(results); // results contains rows returned by server
    console.log(fields); // fields contains extra meta data about results, if available

    // If you execute same statement again, it will be picked from a LRU cache
    // which will save query preparation time and give better performance
  }
);
```

### プール

```ts
const pool = mysql.createPool({
  host: "localhost",
  user: "root",
  database: "test",
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0,
});
```

```ts
// For pool initialization, see above
pool.query("SELECT field FROM atable", function (err, rows, fields) {
  // Connection is automatically released when query resolves
});
```

## 参考

- [sidorares/no-mysql2](https://github.com/sidorares/node-mysql2)
