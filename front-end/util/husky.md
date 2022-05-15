# Husky

Husky は git の commit や push の直前にスクリプトを実行するツールです。

## Installation

```bash
yarn add -D husky
```

## Configuration

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

## References

- [typicode/husky](https://github.com/typicode/husky/tree/master)
