# TIL Personal Wiki 設計書

## 概要

LLMを使って個人ナレッジベース（TIL Wiki）を構築・運用するシステム。
Karpathyの「LLM Knowledge Bases」パターンを踏襲しつつ、ObsidianとMkDocsの両方から参照可能にする。

**コアコンセプト:**
- ソースは単一のMarkdownファイル群。Obsidian（ローカル閲覧・編集）とMkDocs（公開サイト）が同じファイルを参照
- Web記事をObsidian Web Clipperで取り込み、LLM（Claude Code）がWikiへコンパイル
- frontmatterの `public: true` フラグで選択的に公開
- GitHub Pagesにデプロイ

## ディレクトリ構造

```
til/
├── CLAUDE.md                  # LLMエージェント向けスキーマ定義
├── mkdocs.yml                 # MkDocs設定（docs_dir: wiki/）
├── pyproject.toml             # プロジェクト定義 + MkDocs依存
├── uv.lock                    # ロックファイル（自動生成）
├── mkdocs_hooks/
│   └── public_filter.py       # public: trueフィルタリングフック
├── .github/
│   └── workflows/
│       └── deploy.yml         # GitHub Pages自動デプロイ
├── raw/                       # ソース素材（不変、LLMは読み取りのみ）
│   ├── articles/              # Web Clipperでクリップした記事
│   └── assets/                # 画像等
└── wiki/                      # LLMがコンパイルしたWiki本体
    ├── index.md               # カテゴリ別コンテンツカタログ
    ├── log.md                 # 追記専用の活動タイムライン
    ├── concepts/              # トピックページ
    ├── sources/               # 取り込み元のサマリー
    └── assets/                # Wiki内で使う画像
```

### 設計判断

- `raw/` は生素材の保管場所。LLMは読むが書き換えない
- `wiki/` がObsidian Vault兼MkDocsのドキュメントルート
- Karpathyの `entities/` や `comparisons/` は、TILスタイルでは使用頻度が低いため初期構成から省略。必要になったら後から追加可能
- 依存管理は `uv` + `pyproject.toml` を使用

## Markdownファイルフォーマット

各Wikiページは以下のYAML frontmatterを持つ：

```yaml
---
title: Pythonのリスト内包表記
type: concept              # concept | source-summary
sources:                   # raw/内の参照元
  - raw/articles/python-list-comprehension.md
related:                   # 関連Wikiページへのwikilink
  - "[[generator-expression]]"
  - "[[python-performance]]"
created: 2026-04-05
updated: 2026-04-05
public: false              # trueのページのみMkDocsで公開
tags:
  - python
  - syntax
---
```

### 規約

- `public` のデフォルトは `false`（明示的に `true` にしたページのみ公開）
- `type` は2種: `concept`（学んだ知識）と `source-summary`（取り込み元の要約）
- `tags` はObsidianのタグ検索とMkDocs Material のタグ機能の両方で活用
- 本文中のリンクは全て `[[wikilink]]` 記法で統一
- ファイル名はケバブケース（例: `list-comprehension.md`）
- `log.md` の形式: `## [YYYY-MM-DD] operation-type | 説明`

## Obsidian + MkDocs 互換性

### MkDocsプラグイン構成

```yaml
plugins:
  - search
  - obsidian-links             # [[wikilinks]] → 標準リンクに変換
  - tags                       # frontmatterのtagsを活用
  - mkdocs-exclude:
      glob:
        - "*.exclude"

markdown_extensions:
  - meta                       # frontmatter読み取り
  - admonition                 # コールアウト対応
  - pymdownx.tasklist          # チェックリスト対応
```

### 公開フィルタリング

MkDocsのhook機能で `public: true` でないページをビルドから除外する：

```python
# mkdocs_hooks/public_filter.py
import yaml

def on_files(files, config):
    """public: true でないページをビルドから除外"""
    filtered = []
    for file in files:
        if not file.src_path.endswith('.md'):
            filtered.append(file)
            continue
        with open(file.abs_src_path, 'r') as f:
            content = f.read()
        if content.startswith('---'):
            fm = yaml.safe_load(content.split('---')[1])
            if fm and fm.get('public') is True:
                filtered.append(file)
    files._files = filtered
    return files
```

`mkdocs.yml` に `hooks: [mkdocs_hooks/public_filter.py]` を追加して連携。

### 互換性マトリクス

| 機能 | Obsidian | MkDocs |
|------|----------|--------|
| `[[wikilinks]]` | ネイティブ | プラグインで変換 |
| frontmatter tags | タグペイン | Material tags機能 |
| 画像 `![[image.png]]` | ネイティブ | プラグインで変換 |
| コールアウト `> [!note]` | ネイティブ | admonition拡張で近似 |
| バックリンク | ネイティブ | 非対応（許容） |

## CLAUDE.md（LLMエージェント向けスキーマ）

LLMがWikiを操作する際の3つのコア操作を定義する：

### Ingest（取り込み）

1. `raw/` 内の新規ソースを読む
2. `wiki/sources/` にサマリーページを作成
3. 関連する `wiki/concepts/` ページを更新または新規作成
4. `wiki/index.md` にエントリ追加
5. `wiki/log.md` に記録を追記
6. 既存Wikiとの矛盾があればフラグを立てる

### Query（質問）

1. `wiki/index.md` で関連ページを特定
2. 該当ページを読んで回答を合成
3. `[[wikilink]]` でソースを引用
4. 有用な回答は新しいWikiページとして保存

### Lint（整合性チェック）

- ページ間の矛盾を検出
- インバウンドリンクのない孤立ページを検出
- 言及されているが専用ページのないコンセプトを検出
- 古くなった情報を検出

## GitHub Actions デプロイ

```yaml
# .github/workflows/deploy.yml
name: Deploy Wiki to GitHub Pages

on:
  push:
    branches: [main]
    paths: [wiki/**, mkdocs.yml]

permissions:
  pages: write
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v6
      - run: uv sync
      - run: uv run mkdocs build --strict
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site/
      - id: deployment
        uses: actions/deploy-pages@v4
```

### 設計判断

- `wiki/` か `mkdocs.yml` に変更があったときだけトリガー（`raw/` の変更ではビルドしない）
- `--strict` で壊れたリンク等があればビルドを失敗させる
- `uv sync` + `uv run` で依存管理

## 参考

- [Karpathy's LLM Knowledge Bases tweet](https://x.com/karpathy/status/2039805659525644595)
- [Karpathy's LLM Wiki: The Complete Guide](https://antigravity.codes/blog/karpathy-llm-wiki-idea-file)
- [mkdocs-obsidian-links plugin](https://github.com/mara-Li/mkdocs-obsidian-links)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
