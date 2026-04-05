# Today I Learned

## スキーマ

### ディレクトリ構造
- `raw/articles/` — Web Clipperで取り込んだ記事（読み取り専用）
- `raw/assets/` — 画像等（読み取り専用）
- `wiki/` — コンパイル済みWiki
  - `index.md` — カテゴリ別カタログ（`public: true`）
  - `log.md` — 活動タイムライン（`public: true`）
  - `concepts/` — 学習トピックページ
  - `sources/` — 取り込み元サマリー
  - `assets/` — Wiki用画像

### ページ規約

- frontmatter必須フィールド: title, type, sources, related, created, updated, public, tags
- `public` ���デフォルトは `true`
- リンクは `[[wikilink]]` 記法で統一
- ファイル名はケバブケース（例: `list-comprehension.md`）
- `public: true` のページは他の `public: true` のページにのみリンクすること

### frontmatterテンプレート

```yaml
---
title: ページタイトル
type: concept              # concept | source-summary
sources:                   # raw/内の参照元
  - raw/articles/example.md
related:                   # 関連Wikiページへのwikilink
  - "[[related-page]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
public: true
tags:
  - tag-name
---
```

### 操作

スキルとして定義済み。`/ingest`、`/query`、`/lint` で呼び出す。
