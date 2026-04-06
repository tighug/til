import glob
import os
import re

import yaml

WIKI_DIR = os.path.join(os.path.dirname(__file__), "..", "wiki")
REQUIRED_FIELDS = ["title", "type", "sources", "related", "created", "updated", "public", "tags"]


def _wiki_md_files():
    """wiki/ 配下の全 .md ファイルパスを返す"""
    return sorted(glob.glob(os.path.join(WIKI_DIR, "**", "*.md"), recursive=True))


def _parse_frontmatter(filepath):
    """YAML frontmatter を辞書として返す。なければ None。"""
    with open(filepath) as f:
        content = f.read()
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    return yaml.safe_load(parts[1])


class TestFrontmatterRequired:
    def test_all_pages_have_required_fields(self):
        errors = []
        for filepath in _wiki_md_files():
            fm = _parse_frontmatter(filepath)
            if fm is None:
                rel = os.path.relpath(filepath, WIKI_DIR)
                errors.append(f"{rel}: frontmatter がありません")
                continue
            rel = os.path.relpath(filepath, WIKI_DIR)
            for field in REQUIRED_FIELDS:
                if field not in fm:
                    errors.append(f"{rel}: 必須フィールド '{field}' がありません")
        assert not errors, "frontmatter エラー:\n" + "\n".join(errors)


def _extract_wikilinks(filepath):
    """ファイルの本文と frontmatter related から [[wikilink]] を抽出"""
    with open(filepath) as f:
        content = f.read()
    return re.findall(r"\[\[([^\]]+)\]\]", content)


def _resolve_wikilink(name):
    """wikilink名をファイルパスに解決。見つからなければ None。"""
    name = name.split("|")[0]
    for subdir in ["concepts", "sources", ""]:
        candidate = os.path.join(WIKI_DIR, subdir, f"{name}.md")
        if os.path.isfile(candidate):
            return candidate
    return None


class TestWikilinkIntegrity:
    def test_public_pages_link_only_to_public_pages(self):
        errors = []
        for filepath in _wiki_md_files():
            fm = _parse_frontmatter(filepath)
            if fm is None or fm.get("public") is not True:
                continue
            rel = os.path.relpath(filepath, WIKI_DIR)
            for link in _extract_wikilinks(filepath):
                target = _resolve_wikilink(link)
                if target is None:
                    errors.append(f"{rel}: [[{link}]] のリンク先が存在しません")
                    continue
                target_fm = _parse_frontmatter(target)
                if target_fm is None or target_fm.get("public") is not True:
                    errors.append(f"{rel}: [[{link}]] のリンク先が public: true ではありません")
        assert not errors, "wikilink エラー:\n" + "\n".join(errors)


KEBAB_CASE_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")
ALLOWED_NAMES = {"index.md", "log.md"}


class TestFilenameConvention:
    def test_all_md_files_are_kebab_case(self):
        errors = []
        for filepath in _wiki_md_files():
            filename = os.path.basename(filepath)
            if filename in ALLOWED_NAMES:
                continue
            if not KEBAB_CASE_RE.match(filename):
                rel = os.path.relpath(filepath, WIKI_DIR)
                errors.append(f"{rel}: ファイル名がケバブケースではありません")
        assert not errors, "ファイル名エラー:\n" + "\n".join(errors)


class TestIndexSync:
    def test_all_concepts_listed_in_index(self):
        index_path = os.path.join(WIKI_DIR, "index.md")
        with open(index_path) as f:
            index_content = f.read()
        index_links = set(re.findall(r"\[\[([^\]]+)\]\]", index_content))

        concept_dir = os.path.join(WIKI_DIR, "concepts")
        concept_files = glob.glob(os.path.join(concept_dir, "*.md"))

        orphans = []
        for filepath in concept_files:
            name = os.path.splitext(os.path.basename(filepath))[0]
            if name not in index_links:
                orphans.append(name)
        assert not orphans, "index.md に未掲載のコンセプト:\n" + "\n".join(orphans)
