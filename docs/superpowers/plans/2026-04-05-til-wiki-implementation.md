# Today I Learned Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Karpathyスタイルの LLM 駆動 Today I Learned Wiki を構築し、Obsidian と MkDocs (Material) の両方から参照可能にする

**Architecture:** `wiki/` ディレクトリを Obsidian Vault 兼 MkDocs ドキュメントルートとして共有。`[[wikilinks]]` は Obsidian でネイティブ動作し、MkDocs では ezlinks プラグインでビルド時変換。`public: true` frontmatter による選択的公開を MkDocs フックで実現。

**Tech Stack:** MkDocs + Material theme, mkdocs-obsidian-links (ezlinks), mkdocs-callouts, uv, GitHub Actions, GitHub Pages

**Spec:** `docs/superpowers/specs/2026-04-05-til-wiki-design.md`

---

## File Structure

| Action | Path | Responsibility |
|--------|------|----------------|
| Create | `.gitignore` | ビルド成果物・Obsidian設定の除外 |
| Create | `pyproject.toml` | プロジェクト定義 + MkDocs依存 |
| Create | `mkdocs.yml` | MkDocs設定（テーマ、プラグイン、フック） |
| Create | `mkdocs_hooks/__init__.py` | パッケージ初期化（空ファイル） |
| Create | `mkdocs_hooks/public_filter.py` | `public: true` フィルタリングフック |
| Create | `tests/test_public_filter.py` | フックのユニットテスト |
| Create | `wiki/index.md` | カテゴリ別コンテンツカタログ |
| Create | `wiki/log.md` | 活動タイムライン |
| Create | `wiki/concepts/.gitkeep` | ディレクトリ保持 |
| Create | `wiki/sources/.gitkeep` | ディレクトリ保持 |
| Create | `wiki/assets/.gitkeep` | ディレクトリ保持 |
| Create | `raw/articles/.gitkeep` | ディレクトリ保持 |
| Create | `raw/assets/.gitkeep` | ディレクトリ保持 |
| Create | `CLAUDE.md` | LLMエージェント向けスキーマ |
| Create | `.github/workflows/deploy.yml` | GitHub Pages自動デプロイ |
| Modify | `README.md` | プロジェクト説明を更新 |

---

## Task 1: プロジェクト基盤

**Files:**
- Create: `.gitignore`
- Create: `pyproject.toml`

- [ ] **Step 1: `.gitignore` を作成**

```gitignore
# MkDocs build output
site/

# Obsidian
.obsidian/

# Python
__pycache__/
*.pyc
.venv/
```

- [ ] **Step 2: `pyproject.toml` を作成**

```toml
[project]
name = "til"
version = "0.1.0"
description = "LLM-powered Today I Learned wiki with Obsidian + MkDocs"
requires-python = ">=3.12"
dependencies = [
    "mkdocs",
    "mkdocs-material",
    "mkdocs-obsidian-links",
    "mkdocs-callouts",
    "pyyaml",
]

[dependency-groups]
dev = [
    "pytest",
]

[tool.pytest.ini_options]
pythonpath = ["."]
```

- [ ] **Step 3: `uv sync` で依存をインストール**

Run: `uv sync`
Expected: `.venv/` と `uv.lock` が生成される

- [ ] **Step 4: コミット**

```bash
git add .gitignore pyproject.toml uv.lock
git commit -m "feat: add project scaffolding with uv and MkDocs dependencies"
```

---

## Task 2: MkDocs 設定

**Files:**
- Create: `mkdocs.yml`

- [ ] **Step 1: `mkdocs.yml` を作成**

```yaml
site_name: Today I Learned
site_description: LLM-powered personal knowledge base
docs_dir: wiki

theme:
  name: material

plugins:
  - search
  - ezlinks
  - callouts
  - tags

hooks:
  - mkdocs_hooks/public_filter.py

markdown_extensions:
  - nl2br
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tasklist
```

- [ ] **Step 2: コミット**

```bash
git add mkdocs.yml
git commit -m "feat: add MkDocs configuration with Obsidian compatibility plugins"
```

---

## Task 3: 公開フィルタリングフック（TDD）

**Files:**
- Create: `mkdocs_hooks/__init__.py`
- Create: `mkdocs_hooks/public_filter.py`
- Create: `tests/test_public_filter.py`

- [ ] **Step 1: `mkdocs_hooks/__init__.py` を作成（空ファイル）**

```bash
mkdir -p mkdocs_hooks
touch mkdocs_hooks/__init__.py
```

- [ ] **Step 2: テストを書く**

```python
# tests/test_public_filter.py
import tempfile
import os
from pathlib import Path
from unittest.mock import MagicMock

from mkdocs_hooks.public_filter import on_files


def _make_file(tmp_dir, src_path, content):
    """テスト用のMkDocs Fileオブジェクトを作成"""
    abs_path = os.path.join(tmp_dir, src_path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    with open(abs_path, "w") as f:
        f.write(content)
    file = MagicMock()
    file.src_path = src_path
    file.abs_src_path = abs_path
    return file


def _make_files(file_list):
    """MkDocs Filesオブジェクトをモック"""
    files = MagicMock()
    files.__iter__ = MagicMock(return_value=iter(file_list))
    removed = []
    files.remove = MagicMock(side_effect=lambda f: removed.append(f))
    files._removed = removed
    return files


class TestPublicFilter:
    def test_keeps_public_true_page(self, tmp_path):
        f = _make_file(
            str(tmp_path),
            "concepts/test.md",
            "---\ntitle: Test\npublic: true\n---\n# Test",
        )
        files = _make_files([f])
        on_files(files, {})
        assert f not in files._removed

    def test_removes_public_false_page(self, tmp_path):
        f = _make_file(
            str(tmp_path),
            "concepts/private.md",
            "---\ntitle: Private\npublic: false\n---\n# Private",
        )
        files = _make_files([f])
        on_files(files, {})
        assert f in files._removed

    def test_removes_page_without_frontmatter(self, tmp_path):
        f = _make_file(
            str(tmp_path),
            "concepts/no-fm.md",
            "# No Frontmatter",
        )
        files = _make_files([f])
        on_files(files, {})
        assert f in files._removed

    def test_removes_page_without_public_field(self, tmp_path):
        f = _make_file(
            str(tmp_path),
            "concepts/no-public.md",
            "---\ntitle: No Public\n---\n# No Public",
        )
        files = _make_files([f])
        on_files(files, {})
        assert f in files._removed

    def test_keeps_non_markdown_files(self, tmp_path):
        f = _make_file(
            str(tmp_path),
            "assets/image.png",
            "fake image data",
        )
        files = _make_files([f])
        on_files(files, {})
        assert f not in files._removed

    def test_mixed_files(self, tmp_path):
        public = _make_file(
            str(tmp_path),
            "concepts/public.md",
            "---\ntitle: Public\npublic: true\n---\n# Public",
        )
        private = _make_file(
            str(tmp_path),
            "concepts/private.md",
            "---\ntitle: Private\npublic: false\n---\n# Private",
        )
        image = _make_file(
            str(tmp_path),
            "assets/img.png",
            "fake",
        )
        files = _make_files([public, private, image])
        on_files(files, {})
        assert private in files._removed
        assert public not in files._removed
        assert image not in files._removed
```

- [ ] **Step 3: テストが失敗することを確認**

Run: `uv run pytest tests/test_public_filter.py -v`
Expected: FAIL（`mkdocs_hooks.public_filter` に `on_files` が見つからない）

- [ ] **Step 4: フックを実装**

```python
# mkdocs_hooks/public_filter.py
import yaml


def on_files(files, config):
    """public: true でないページをビルドから除外"""
    to_remove = []
    for file in files:
        if not file.src_path.endswith('.md'):
            continue
        with open(file.abs_src_path, 'r') as f:
            content = f.read()
        if content.startswith('---'):
            fm = yaml.safe_load(content.split('---')[1])
            if not (fm and fm.get('public') is True):
                to_remove.append(file)
        else:
            to_remove.append(file)
    for file in to_remove:
        files.remove(file)
    return files
```

- [ ] **Step 5: テストが通ることを確認**

Run: `uv run pytest tests/test_public_filter.py -v`
Expected: 6 passed

- [ ] **Step 6: コミット**

```bash
git add mkdocs_hooks/ tests/
git commit -m "feat: add public filter hook with tests"
```

---

## Task 4: Wiki 初期構造

**Files:**
- Create: `wiki/index.md`
- Create: `wiki/log.md`
- Create: `wiki/concepts/.gitkeep`
- Create: `wiki/sources/.gitkeep`
- Create: `wiki/assets/.gitkeep`
- Create: `raw/articles/.gitkeep`
- Create: `raw/assets/.gitkeep`

- [ ] **Step 1: ディレクトリ構造を作成**

```bash
mkdir -p wiki/concepts wiki/sources wiki/assets raw/articles raw/assets
touch wiki/concepts/.gitkeep wiki/sources/.gitkeep wiki/assets/.gitkeep
touch raw/articles/.gitkeep raw/assets/.gitkeep
```

- [ ] **Step 2: `wiki/index.md` を作成**

```markdown
---
title: Index
type: concept
sources: []
related: []
created: 2026-04-05
updated: 2026-04-05
public: true
tags: []
---

# Today I Learned

## Categories

(LLMがIngest時に自動更新)
```

- [ ] **Step 3: `wiki/log.md` を作成**

```markdown
---
title: Activity Log
type: concept
sources: []
related: []
created: 2026-04-05
updated: 2026-04-05
public: true
tags: []
---

# Activity Log

## 2026-04-05 init | Wiki初期構造を作成
```

- [ ] **Step 4: コミット**

```bash
git add wiki/ raw/
git commit -m "feat: add initial wiki structure with index and log"
```

---

## Task 5: CLAUDE.md

**Files:**
- Create: `CLAUDE.md`

- [ ] **Step 1: `CLAUDE.md` を作成**

```markdown
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
```

- [ ] **Step 2: コミット**

```bash
git add CLAUDE.md
git commit -m "feat: add CLAUDE.md with LLM agent schema"
```

---

## Task 6: GitHub Actions デプロイ

**Files:**
- Create: `.github/workflows/deploy.yml`

- [ ] **Step 1: ワークフローを作成**

```yaml
# .github/workflows/deploy.yml
name: Deploy Wiki to GitHub Pages

on:
  push:
    branches: [main]
    paths: [wiki/**, mkdocs.yml, mkdocs_hooks/**, pyproject.toml]

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
      - uses: astral-sh/setup-uv@v5
      - run: uv sync
      - run: uv run mkdocs build --strict
      - uses: actions/upload-pages-artifact@v4
        with:
          path: site/
      - id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 2: コミット**

```bash
git add .github/
git commit -m "feat: add GitHub Actions workflow for Pages deployment"
```

---

## Task 7: README 更新

**Files:**
- Modify: `README.md`

- [ ] **Step 1: `README.md` を更新**

```markdown
# Today I Learned

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
```

- [ ] **Step 2: コミット**

```bash
git add README.md
git commit -m "docs: update README with project overview and usage"
```

---

## Task 8: End-to-End 検証

- [ ] **Step 1: ローカルビルドを実行**

Run: `uv run mkdocs build --strict`
Expected: `site/` ディレクトリが生成され、`index.html` と `log/index.html` が含まれる（`public: true` のページのみ）

- [ ] **Step 2: ローカルサーバーで確認（手動）**

Run: `uv run mkdocs serve &`
Run: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000`
Expected: `200`
Run: `kill %1`

（オプション: ブラウザで `http://127.0.0.1:8000` を開いて目視確認）

- [ ] **Step 3: テスト全体を実行**

Run: `uv run pytest tests/ -v`
Expected: All passed

- [ ] **Step 4: 非公開ページがビルドから除外されることを確認**

```bash
# テスト用の非公開ページを作成
cat > wiki/concepts/test-private.md << 'EOF'
---
title: Test Private
type: concept
sources: []
related: []
created: 2026-04-05
updated: 2026-04-05
public: false
tags: []
---
# This should not appear in the build
EOF

# リビルド
uv run mkdocs build --strict

# 非公開ページが含まれていないことを確認
test ! -d site/concepts/test-private/ && echo "PASS: private page excluded" || echo "FAIL: private page included"

# クリーンアップ
rm wiki/concepts/test-private.md
rm -rf site/
```

- [ ] **Step 5: 問題があれば修正してコミット**
