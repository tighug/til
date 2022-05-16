# Husky

Huskyはgitのcommitやpushの前にスクリプトを走らせるツールです。

## インストール

=== "npm"

    ```bash
    npm install -D husky
    ```

=== "yarn"

    ```bash
    yarn add -D husky
    ```

## 設定

`package.json`あるいは`.hukyrc`ファイルに記述します。

```json
// package.json
{
    "husky": {
        "hooks": {
            "pre-commit": "npm test",
            "pre-push": "npm test",
            "...": "..."
        }
    }
}
```

```json
// .huskyrc
{
    "hooks": {
        "pre-commit": "npm test"
    }
}
```

## 参考

- [typicode/husky](https://github.com/typicode/husky/tree/master)
