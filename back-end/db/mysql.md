# MySQL

MySQL とは、**データベース管理システム（DBMS）のひとつ**です。

- [MySQL の使い方を基礎からマスター](https://26gram.com/mysql)

## Installation

### Linux

```bash
sudo apt update
sudo apt install mysql-server
```

### Mac

```bash
brew update
brew install mysql
```

## Usage

起動・停止・再起動・状態確認

```bash
sudo service mysql start  // 起動
sudo service mysql stop // 停止
sudo service mysql restart // 再起動
sudo service mysql status // 状態
```

ログイン

```bash
sudo mysql -u root -p // root
sudo mysql -u [user] -p // user
```

ログアウト

```sql
exit
```

## Command

### ユーザーの管理

- **作成**

  ```sql
  CREATE USER ['user']@['host'] IDENTIFIED BY ['password'];
  ```

- **確認**

  ```sql
  SELECT USER, HOST FROM mysql.user;
  ```

- **権限付与**

  ```sql
  GRANT ALL PRIVILEGES ON *.* TO ['user']@['host'];
  ```

- **権限確認**

  ```sql
  SHOW GRANTS FOR [user]@[host];
  ```

### データベースの管理

- **作成**

  ```sql
  CREATE DATABASE [name];
  ```

- **一覧**

  ```sql
  SHOW DATABASES;
  ```

- **指定**

  ```sql
  USE [db name];
  ```

- **削除**

  ```sql
  DROP DATABASE [name];
  ```

### テーブルの管理

- **作成**

  ```sql
  CREATE TABLE [name] (
      [field name] [data type] [option]
  );
  ```

  - `PRIMARY KEY`：主キー
  - `UNIQUE`：重複を許容しない
  - `NOT NULL`：NULL を許容しない
  - `DEFAULT [value]`：デフォルト値

- **確認**

  ```sql
  SHOW TABLES;
  ```

- **構造確認**

  ```sql
  DESC [name];
  ```

- **削除**

  ```sql
  DROP TABLE [name];
  ```

### レコードの管理

- **追加**

  ```sql
  INSERT INTO [table name] [field name] VALUES [value];
  ```

- **取得**

  ```sql
  SELECT [field name] FROM [table name];
  ```

- **列追加**

  ```sql
  ALTER TABLE [table name] ADD COLUMN [field name] [data type]
  ```

- **更新**

  ```sql
  UPDATE [table name] SET [field name]=[value] WHERE [conditional];
  ```

- **削除**

  ```sql
  DELETE FROM [table name];                     # 全削除
  DELETE FROM [table name] WHERE [conditional]; # 一部削除
  ```

#### クエリ

レコード取得の際のクエリ。

| query         | description    |
| ------------- | -------------- |
| `AS`          | 別名を付ける   |
| `DISTINCT`    | 重複を除外     |
| `WHERE`       | 抽出           |
| `LIKE`        | あいまい抽出   |
| `IS NULL`     | `== null`      |
| `IS NOT NULL` | `!= null`      |
| `BETWEEN`     | 範囲           |
| `AND`         | かつ           |
| `OR`          | もしくは       |
| `ORDER BY`    | 昇順 / 降順    |
| `LIMIT`       | レコード数制限 |
| `CASE`        | 条件分岐       |

#### example

```sql
SELECT name AS 'Titles' FROM movies;            # AS
SELECT DISTINCT tooles FROM inventory;          # DISTINCT
SELECT * FROM movies WHERE imdb_rating > 8;     # WHERE
SELECT * FROM movies WHERE name LIKE 'Se_en';   # LIKE 1
SELECT * FROM movies WHERE name LIKE '%man%';   # LIKE 2
SELECT name FROM movies WHERE imdb_rating IS NOT NULL;  # IS NOT NULL
SELECT * FROM movies WHERE year BETWEEN 1990 AND 1999;  # BETWEEN
SELECT * FROM movies WHERE year BETWEEN 1990 AND 1999 AND genre = 'romance';  # AND
SELECT * FROM movies WHERE year > 2014 OR genre = 'action'; # OR
SELECT * FROM movies ORDER BY name; # ORDER BY
SELECT * FROM movies LIMIT 10;      # LIMIT

# CASE
SELECT name,
  CASE
    WHEN imdb_rating > 8 THEN 'Fantastic'
    WHEN imdb_rating > 6 THEN 'Poorly Received'
    ELSE 'Avoid at All Costs'
  END
FROM movies;
```

##### Aggregate Functions

| function      | description     |
| ------------- | --------------- |
| `COUNT()`     | レコード数      |
| `SUM()`       | 合計            |
| `MAX()/MIN()` | 最大値 / 最小値 |
| `AVG()`       | 平均            |
| `ROUND()`     | 丸め            |
| `GROUNP BY`   | グループ化      |
| `HAVING`      | 抽出条件        |

## データ型

### 整数

|                | 型            | 値の範囲                                    |
| -------------- | ------------- | ------------------------------------------- |
| `TYNYINT(m)`   | 整数（1byte） | -128 ～ 127                                 |
| `SMALLINT(m)`  | 整数（2byte） | -32768 ～ 32767                             |
| `MEDIUMINT(m)` | 整数（3byte） | -8388608 ～ 8388607                         |
| `INT(m)`       | 整数（4byte） | -2147483648 ～ 2147483647                   |
| `BIGINT(m)`    | 整数（8byte） | -9223372036854775808 ～ 9223372036854775807 |

- `UNSIGNED`：正の数に限定する
- `ZEROFILL`:入力した数字に対して最大桁数までゼロで埋める

### 小数

|               | 型                 | 値の範囲                                            |
| ------------- | ------------------ | --------------------------------------------------- |
| `FLOAT`       | 単精度浮動小数点型 | 3.402823466E+38 ～ 3.402823466E+38                  |
| `DOUBLE`      | 倍精度浮動小数点型 | -1.7976931348623157E+308 ～ 1.7976931348623157E+308 |
| `FLOAT(m,d)`  | 単精度浮動小数点型 | m：1 ～ 255 桁 n：0 ～ 30 桁まで指定可能            |
| `DOUBLE(m,d)` | 倍精度浮動小数点型 | m：1 ～ 255 桁 n：0 ～ 30 桁まで指定可能            |

- `UNSIGNED`：正の数に限定する
- `ZEROFILL`:入力した数字に対して最大桁数までゼロで埋める

### 文字列

|              | 型           | 値の範囲                             |
| ------------ | ------------ | ------------------------------------ |
| `CHAR(m)`    | 固定長文字型 | m（文字数指定）：0 ～ 255 文字       |
| `VARCHAR(m)` | 可変長文字型 | m（バイト数指定）：0 ～ 65535 バイト |
| `TYNYTEXT`   | テキスト型   | 0 ～ 255 バイト（固定）              |
| `TEXT`       | テキスト型   | 0 ～ 65535 バイト（固定）            |
| `MEDIUMTEXT` | テキスト型   | 0 ～ 16777215 バイト（固定）         |
| `LONGTEXT`   | テキスト型   | 0 ～ 4294967295 バイト（固定）       |

### 日付・時刻

|             | 型           | 基本フォーマット      | 備考                      |
| ----------- | ------------ | --------------------- | ------------------------- |
| `DATE`      | 日付         | 'YYYY-MM-DD'          |                           |
| `DATETIME`  | 日付時刻     | 'YYYY-MM-DD HH:MM:SS' |                           |
| `TIMESTAMP` | 日付時刻     | 'YYYY-MM-DD HH:MM:SS' |                           |
| `TIME`      | 時刻         | 'HH:MM:SS'            |                           |
| `YEAR[4]`   | 日付（4 桁） | 'YYYY'                | 1901 ～ 2155, 0000        |
| `YEAR[2]`   | 日付（2 桁） | 'YY'                  | 70 ～ 69 （1970 ～ 2069） |

### バイナリ

## CSV ファイルの入出力

### CSV から MySQL

```sql
LOAD DATA INFILE '[csv name]' INTO TABLE [table name]
  FIELDS
    TERMINATED BY ','
    ENCLOSED BY '"'
  LINES
    TERMINATED BY '\r\n'
  IGNORE [整数] LINES;
```

#### オプションの詳細

FIELD オプションは 3 つ。変更が不要な場合は省略可能。

| option          | description          |
| --------------- | -------------------- |
| `TERMINATED BY` | 区切り文字           |
| `ENCLOSED BY`   | 囲み文字             |
| `ESCAPED BY`    | エスケープシーケンス |

LINES オプション。

| option          | description |
| --------------- | ----------- |
| `TERMINATED BY` | 改行コード  |

IGNORE オプションは、**整数**で指定した行を取り込み対象外にする。
