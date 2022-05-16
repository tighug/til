# ESLint

ESLint とは、**JavaScript のための静的検証ツール**の一つです。

## Installation

=== "Yarn"

    ```bash
    yarn add -D eslint
    ```

=== "NPM"

    ```bash
    npm install -D eslint
    ```

## CUI

```bash
eslint [file] # Linting file

eslint --init # Generate .eslintrc.js
```

## Configuration

`.eslintrc`に記述します。

### `extends`

既存の設定を拡張します。できる限り`extends`で対応し、オリジナルの設定のみ個別で上書きすると楽です。

### `plugins`

使用したいプラグインを記述します。大体`extends`と関係します。

### `parser`

使用したいパーサーを記述します。TypeScript や Babel 等、使いたい言語に合わせて変更します。

### `parseOptions`

ES6 の`import/export`を使いたい場合、以下で ES Modules 機能を有効にします。

```json
{
  "parserOptions": {
    "sourceType": "module"
  }
}
```

### `env`

最低限、以下の三つを設定します。他は`extends`で`recommended`を選択すると大体自動で設定してくれます。

```json
{
  "env": {
    "browser": true, // ブラウザで実行する
    "node": true, // Node.jsで実行する
    "es6": true // ES6を使用する
  }
}
```

### `rules`

ルールを上書きできます。できる限り`extends`の`recommended`を採用したいので、あまり記述しません。

## Example

ESLint + Prettier + XXX

### Packages

```bash
yarn add -D eslint
yarn add -D prettier eslint-config-prettier eslint-plugin-prettier

yarn add -D @typescript-eslint/eslint-plugin  # When uging TyepScript
yarn add -D @typescript-eslint/parser         # When using TypeScript
yarn add -D eslint-plugin-react # When using React
yarn add -D eslint-plugin-vue   # When using Vue
```

### .eslintrc.json

```json
{
  "env": {
    "browser": true,
    "es6": true,
    "node": true,
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",  // When using TypeScript
    "plugin:react/recommended",     // When using React
    "plugin:vue/recommended",       // When using Vue
    "plugin:prettier/recommended",
    "prettier/@typescript-eslint",  // When using TypeScript
    "prettier/babel"                // When using JavaScript
    "prettier/react",               // When using React
    "prettier/vue"                  // When using Vue
  ],
  "parser": "@typescript-eslint/parser",  // When using TypeScript
  "parseOptions": {
    "sourceType": "module",         // When using ES6 import/export
    "ecmaFeatures": {               // When using React
      "jsx": true
    }
  },
  // Need installing the plugin to use
  "plugins": [
    "@typescript-eslint",           // When using TypeScript
    "babel",                        // When using JavaScript
    "react",                        // When using React
    "vue"                           // When using Vue
  ],
  "rules": {}
}
```

## References

- [ESLint](https://eslint.org/)
- [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier)
- [eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier)
- [Prettier 入門 ～ ESLint との違いを理解して併用する～ - Qiita](https://qiita.com/soarflat/items/06377f3b96964964a65d)
- [ESLint 最初の一歩 | Qiita](https://qiita.com/mysticatea/items/f523dab04a25f617c87d)
