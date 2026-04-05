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
