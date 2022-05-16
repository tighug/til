# Babel

Babel は、ES6 以降の JavaScript コードを ES5 以前の下位互換バージョンに変換するツールチェーンです。TypeScript を使う場合には、基本的に使用する必要はありませんが、Babel に依存しているパッケージ（`styled-components`や`react-hot-loader`）を使いたい場合には併用します。

## Installation

どのような環境でも以下の二つはほぼ必須です。

```bash
yarn add -D @babel/core # Babel本体
yarn add -D @babel/preset-env # ターゲット環境に応じたプリセット
```

### CLI

```bash
yarn add -D @babel/cli  # Babel CLI
```

### With React

```bash
yarn add -D @babel/preset-react # React用プリセット
```

### With TypeScript

```bash
yarn add -D @babel/preset-typescript  # TypeScript用プリセット
```

## Configuration

`babel.config.json`に記述します。

```json
{
  "presets": [
    [
      "@babel/env",
      {
        // 必要なcore-jsを自動でimportする
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
