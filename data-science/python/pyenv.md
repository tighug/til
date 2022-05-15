# pyenv

pyenv は Python のバージョン切り替えを行うツールです。

## Installation

```bash
brew install pyenv
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile # For Zsh
```

## Usage

```bash
# インストール可能なバージョンを表示
pyenv install --list

# 特定のバージョンをインストール
pyenv install 3.8.3

# グローバルで特定のバージョンを使用するように設定
pyenv global 3.8.3

# ローカルで特定のバージョンを使用するように設定
# ローカルディレクトリに.python-versionファイルが作成される
pyenv locall 3.8.3
```

## Refernces

- [pyenv/pyenv](https://github.com/pyenv/pyenv)
