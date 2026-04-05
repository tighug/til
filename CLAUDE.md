# TIL Personal Wiki

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
- `public` のデフォルトは `false`
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
public: false
tags:
  - tag-name
---
```

### 操作

#### Ingest（取り込み）
1. `raw/` 内の新規ソースを読む
2. `wiki/sources/` にサマリーページを作成
3. 関連する `wiki/concepts/` ページを更新または新規作成
4. `wiki/index.md` にエントリ追加
5. `wiki/log.md` に `## YYYY-MM-DD ingest | 説明` 形式で記録を追記
6. 既存Wikiとの矛盾があればフラグを立てる
7. `public: true` のページ内のリンク先が全て公開ページであることを確認

#### Query（質問）
1. `wiki/index.md` で関連ページを特定
2. 該当ページを読んで回答を合成
3. `[[wikilink]]` でソースを引用
4. 有用な回答は新しいWikiページとして保存

#### Lint（整合性チェック）
- ページ間の矛盾を検出
- インバウンドリンクのない孤立ページを検出
- 言及されているが専用ページのないコンセプトを検出
- 古くなった情報を検出
- `public: true` のページが非公開ページにリンクしていないか検出
