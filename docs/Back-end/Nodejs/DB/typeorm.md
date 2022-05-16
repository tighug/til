# TypeORM

## インストール

```bash
yarn add typeorm
yarn add reflect-metadata
yarn add -D @types/node

# Chose the database driver you need
yarn add mysql2 # MySQL
yarn add pg # PostgreSQL
yarn add sqlite3  # SQLite
yarn add mongodb  # MongoDB
```

`tsconfig.json`を編集し、デコレータ機能を有効にする。

```json
"emitDecoratorMetadata": true,
"experimentalDecorators": true,
```

## 使い方

### Connection

`ormconfig.json`に記述します。

```json
[
  {
    "name": "default",
    "type": "mysql",
    "host": "localhost",
    "port": 3306,
    "username": "test",
    "password": "test",
    "database": "test"
  },
  {
    "name": "second-connection",
    "type": "mysql",
    "host": "localhost",
    "port": 3306,
    "username": "test",
    "password": "test",
    "database": "test"
  }
]
```

| オプション  | 説明 |
| ----------- | ---- |
| name        |      |
| type        |      |
| entities    |      |
| subscribers |      |
| migrations  |      |
| logging     |      |

### Entity

```ts
import { Entity, PrimaryGeneratedColumn, Column } from "typeorm";

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  firstName: string;

  @Column()
  lastName: string;

  @Column()
  isActive: boolean;
}
```

| デコレータ                        | 説明 |
| --------------------------------- | ---- |
| `@PrimaryColumn()`                |      |
| `@PrimaryGeneratedColumn()`       |      |
| `@PrimaryGeneratedColumn("uuid")` |      |
| `@CreateDateColumn()`             |      |
| `@UpdateDateColumn()`             |      |
| `@DeleteDateColumn()`             |      |
| `@VersionColumn()`                |      |

### Relations

### Entity Manager and Rrepository

### Query Builder

### CLI

```bash
typeorm migration:create -n CreateTables
```

```bash
# typeorm -c <your-config-name> migration:{run|revert}
typeorm migration:run
typeorm migration:revert
```

## 参考

- [TypeORM](https://typeorm.io/#/)
