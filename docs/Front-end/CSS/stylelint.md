# stylelint

stylelint は CSS のためのリンターです。

## Installation

```bash
yarn add -D stylelint stylelint-config-recommended

# CSS の記述順序にルールを導入する場合。
yarn add -D stylelint-order
yarn add -D stylelint-config-recess-order

#Prettier と併用したい場合。
yarn add -D stylelint-prettier stylelint-config-prettier
```

## Usage

```bash
yarn stylelint [file]
```

## Configuration

`.stylelintrc.js`ファイルに記述する。

```js
// .stylelintrc.js
module.exports = {
  extends: [
    "stylelint-config-recommended",
    "stylelint-config-recess-order",
    "stylelint-prettier/recommended",
  ],
};
```

## Integrations

- [vscode-stylelint](https://marketplace.visualstudio.com/items?itemName=stylelint.vscode-stylelint)

## References

- [stylelint](https://stylelint.io/)
- [stylelint の導入と VS Code の設定の方法](https://qiita.com/y-w/items/bd7f11013fe34b69f0df)
