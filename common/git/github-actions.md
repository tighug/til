# GitHub Actions

## Configuration

`.github/workflows/`内の YAML ファイルに記述する。

- `name` : ワークフローの名前
- `on` : ワークフローのトリガーイベント
- `jobs` : ジョブグループ
  - `[job name]` : ジョブの名前
    - `runs-on` : 実行環境
    - `steps` : ステップグループ
      - `uses` : 使用するアクション
      - `run` : 実行するコマンド

## References

- [GitHub Actions](https://docs.github.com/ja/actions)
