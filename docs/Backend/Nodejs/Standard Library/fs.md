# fs

Node.js のファイルシステム。全ての fs 操作には同期・非同期の二種類が存在する。

## Installation

`fs`自体は Node.js に付属しているため、インストール無しで使用できる。しかし、ディレクトリの削除等のいくつかのファイル操作がしづらいため、拡張版である[`fs-extra`](https://github.com/jprichardson/node-fs-extra)の使用を推奨する。

=== "NPM"

    ```bash
    npm install -S fs-extra
    ```

=== "Yarn"

    ```bash
    yarn add fs-extra
    ```

## Setup

```ts
import fs from "fs-extra";
```

## Usage

### Directory

Create

```js
// ディレクトリの存在を確認し、無ければ作成する
await fs.ensureDir("./dir");
```

Read

```js
// ディレクトリ内のコンテンツを取得する
const files = await fs.readdir("./dir");
```

Rename

```js
// ディレクトリやファイルの名前を変更する
await fs.rename("./oldDir", "./newDir");
```

Move

```js
// ディレクトリやファイルを移動する
await fs.move("./src", "./dest", { overwrite: true });
```

Copy

```js
// ディレクトリやファイルをコピーする
await fs.copy("./src", "./dest", { overwrite: true });
```

Delete

```js
// ディレクトリを空にする
// ディレクトリが存在しなければ作成する
await fs.emptyDir("./dir");

// ディレクトリを削除する。空でなくても削除可能
await fs.remove("./dir");
```

### File

Create

```js
// ファイルの存在を確認し、無ければ作成する
await fs.ensureFile("./file.txt");
```

Read

```js
// ファイル内のデータを取得する
const data = await fs.readFile("./file.txt");
```

Update

```js
// ファイルを上書きする。親ディレクトリが存在しない場合は作成する
await fs.outputFile("./file.txt", "Hello!");
```

Rename（Dir と同じ）

```js
// ディレクトリやファイルの名前を変更する
await fs.rename("./old.txt", "./new.txt");
```

Move（Dir と同じ）

```js
// ディレクトリやファイルを移動する
await fs.move("./src/file.txt", "./dest/file.txt", { overwrite: true });
```

Copy（Dir と同じ）

```js
// ディレクトリやファイルをコピーする
await fs.copy("./src.txt", "./dest.txt", { overwrite: true });
```

Delete

```js
// ファイルを削除する
await fs.remove("./file.txt");
```

### Stat

```js
// ディレクトリやファイルの状態（Status）を取得する
const stats = await fs.stat("./dir");
```

```js
stats.isFile(); // ファイルかどうか
stats.isDirectory(); // ディレクトリかどうか
```

## References

- [Node.js: fs-extra](https://github.com/jprichardson/node-fs-extra)
- [Node.js File System Module](https://www.w3schools.com/nodejs/nodejs_filesystem.asp)
