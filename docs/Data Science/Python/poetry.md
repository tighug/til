# Poetry

Poetry は Python のパッケージマネージャーです。

## Installation

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

アップデートは次のコマンドで行う。

```bash
poetry self update
```

タブによる補完を有効にする。

```bash
# Bash
poetry completions bash > /etc/bash_completion.d/poetry.bash-completion

# Zsh
poetry completions zsh > ~/.zfunc/_poetry
```

デフォルトでは仮想環境`.venv`がホームディレクトリに作成されるため、プロジェクト内に作成するよう変更する。

```bash
poetry config virtualenvs.in-project true
```

## Usage

| command            | description                                                  |
| ------------------ | ------------------------------------------------------------ |
| `new [name]`       | 新しいプロジェクトを作成                                     |
| `init`             | `pyproject.toml`をインタラクティブに作成                     |
| `install`          | `pyptoject.toml`を読み込み、依存パッケージをインストールする |
| `update`           | 依存パッケージをアップデートする                             |
| `add [package]`    | `dependencies`にパッケージを追加                             |
| `add -D [package]` | `devdependencies`にパッケージを追加                          |
| `remove [package]` | パッケージを削除                                             |
| `run [script]`     | `pyproject.toml`に定義されたスクリプトを実行                 |
| `build`            | パッケージ化する                                             |
| `publish`          | パッケージを公開する（デフォルトは PyPI）                    |

## Configuration

`pyproject.toml`に記述する

以下に重要な項目を抜粋。＊は必須の項目

-   `name`＊ : パッケージ名
-   `version`＊ : バージョン
-   `description`＊ : パッケージの説明
-   `license` : ライセンス
-   `authors`＊ : 作者

## References

-   [python-poetry/poetry](https://github.com/python-poetry/poetry)
-   [python-poetry docs](https://python-poetry.org/docs/)
-   [python-poetry docs（日本語）](https://cocoatomo.github.io/poetry-ja/)
