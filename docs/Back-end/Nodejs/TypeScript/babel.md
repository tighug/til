# Babel

Babel は、ES6 以降の JavaScript コードを ES5 以前の下位互換バージョンに変換するツールチェーンです。TypeScript を使う場合には、基本的に使用する必要はありませんが、Babel に依存しているパッケージ（`styled-components`や`react-hot-loader`）を使いたい場合には併用します。

## Installation

=== "npm"

    ```bash
    npm install -D @babel/core @babel/preset-env @babel/cli

    npm install -D @babel/preset-react # with React
    npm install -D @babel/preset-typescript  # with TypeScript
    ```

=== "yarn"

    ```bash
    yarn add -D @babel/core @babel/preset-env @babel/cli

    yarn add -D @babel/preset-react # with React
    yarn add -D @babel/preset-typescript  # with TypeScript
    ```

## Configuration

`babel.config.json`に記述します。

```json
{
  "presets": [
    [
      "@babel/env",
      {
        "useBuiltIns": "usage"
      }
    ],
    "@babel/preset-react",
    "@babel/preset-typescript"
  ]
}
```

## References

- [Babel](https://babeljs.io/)
