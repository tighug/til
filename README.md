# TIL Wiki

LLM駆動の個人ナレッジベース。Obsidianでローカル閲覧・編集し、MkDocsで選択的に公開。

## セットアップ

```bash
uv sync
```

## ローカルプレビュー

```bash
uv run mkdocs serve
```

## 使い方

1. Web記事をObsidian Web Clipperで `raw/articles/` にクリップ
2. Claude Codeで `Ingest` 操作を実行
3. `wiki/` 配下にコンパイルされたWikiをObsidianで閲覧
4. 公開したいページの frontmatter で `public: true` を設定
5. `main` にプッシュすると GitHub Pages に自動デプロイ
