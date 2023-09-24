# lint-staged

## インストール

=== "npm"

    ```bash
    npm install -D lint-staged
    ```

=== "yarn"

    ```bash
    yarn add -D lint-staged
    ```

## 設定

`package.json`あるいは`lintstagedrc`ファイルに記述します。

```json
// package.json
{
    "lint-staged": {
        "*": "your-cmd"
    }
}
```

```json
{
    "*": "your-cmd"
}
```

## 参考

- [okonet/lint-staged](https://github.com/okonet/lint-staged)
