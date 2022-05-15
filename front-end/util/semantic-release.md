# semantic-release

## Installation

```bash
yarn add -D semantic-release
```

## CLI

```bash
yarn run semantic-release
```

## Release Steps

| step               | description                                                              |
| ------------------ | ------------------------------------------------------------------------ |
| 条件の確認         | リリースのための条件をすべて確認する                                     |
| 最新リリースの取得 | Git タグを解析し、最新のリリースに該当するコミットを取得する             |
| コミットの分析     | 前回のリリース以降に追加されたコミットをもとに、リリースの種類を決定する |
| リリースの確認     | リリースの適合性を確認する                                               |
| ノートの作成       | 前回のリリース以降に追加されたコミットのリリースノートを作成する         |
| Git タグの作成     | 新しいリリースバージョンに対応する Git タグを作成する                    |
| 準備               | リリースを準備する                                                       |
| 発行               | リリースを発行する                                                       |
| 通知する           | 新しいリリースやエラーを通知する                                         |

## Plugins

以下 4 つはデフォルトに含まれているため、追加のインストールは必要ない。

- `@semantic-release/commit-analyzer`
- `@semantic-release/release-notes-generator`
- `@semantic-release/npm`
- `@semantic-release/github`

## References

- [semantic-release](https://semantic-release.gitbook.io/semantic-release/)
