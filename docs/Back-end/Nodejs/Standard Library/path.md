# path

Node.js のパス操作モジュール。インストール無しで使用できる

## Setup

```js
import path from "path";
```

## Usage

```js
path.basename("./dir/file.txt"); // => file.txt
path.basename("./dir/file.txt", ".txt"); // => file.txt
path.dirname("./dir/file.txt"); // => ./dir
path.extname("./dir/file.txt"); // => .txt
path.join("/foo", "bar", "baz/asdf"); // => /foo/bar/baz/asdf
path.parse("/home/user/dir/file.txt");
// => { root: "/",
//      dir: "/home/user/dir",
//      base: "file.txt",
//      ext: ".txt",
//      name: "file"
//    }
```
