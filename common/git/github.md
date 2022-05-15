# GitHub

## Best Practices

- master ブランチに直接プッシュしない
  - GitHub の Setting で保護可能
- レビュー中に認識されないコミットがないか確認する
  - 間違ったメールアドレスを使用する Author により発生する
  - 追跡が困難になるので回避する
- Code Owner 機能を使用する
  - レビュー担当者として自動的に選択される
- 秘密情報を含めない
- 依存関係をコミットしない（`node_modules`等）
- ローカル構成ファイルをコミットしない
- [Gitignore.io](https://www.toptal.com/developers/gitignore)を使用して`.gitignore`ファイルを作成する
- 無効なリポジトリをアーカイブする（「読み取り専用」にする）
- パッケージのバージョンをロックする（`latest`等を使わない）
- 標準パッケージバージョンを指定する
- タスクリストを活用する
- ブランチの命名規則を使用する
  - git-flow、GitHub-flow
- 古いブランチを削除する
- ブランチを最新に保つ
- 非アクティブな GitHub メンバーを削除する
- セキュリティアラートを有効にする

## References

- [Top GitHub best practices guide for developers](https://www.datree.io/resources/github-best-practices)
