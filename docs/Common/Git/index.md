# Git

Git とは、バージョン管理システム（VCS : Version Control System）のひとつで、プログラムのソースコードなどの変更履歴を記録・追跡する。Git により、複数人でのプログラムの共有や、過去のプログラムの復元が可能になる。

## Installation

### Mac

```bash
sudo brew install git
```

### Linux

```bash
sudo apt install git
```

※ WSL 環境の VS Code で使う場合は[ここ](https://qiita.com/xeres/items/ed4d659cfac4a1695f4b)を参照する。

## Overview

### Concept

#### Repository

リポジトリとは、**ファイルの状態を記録する場所**である。リポジトリは、以下の 2 種類に分けられる。

-   **リモートリポジトリ**：専用のサーバに配置して複数人で共有する
-   **ローカルリポジトリ**：ユーザ一人ひとりが利用するために、自分の手元のマシン上に配置する

#### Working Tree

ワーキングツリーとは、**実際に作業をしているディレクトリ**である。ワーキングツリーから直接リポジトリにファイルの変更を記録することはできず、**インデックス**に登録する必要がある。（`add`）

#### Index

インデックスとは、**リポジトリにファイルの変更を記録する準備をする場所**である。ステージング環境とも呼ぶ。インデックスからリポジトリに変更を記録する操作を**コミット**と呼ぶ。（`commit`)

### Flow

#### ローカルからリモート

1. 新しいリポジトリを作成（初回のみ）：`git init`
2. リモートリポジトリを登録（初回のみ）：`git remote add origin [リモートのURL]`
3. インデックスにファイルの変更を登録：`git add [登録したいファイル]`
4. ローカルリポジトリに変更を記録：`git commit -m "[メッセージ]"`
5. リモートリポジトリに変更を同期：`git push -u origin [ブランチ]`

#### リモートからローカル

1. リモートリポジトリをローカルに複製：`git clone [リモートのURL]`
2. リモートリポジトリから変更を同期：`git pull origin [ブランチ]`

## Setup

リモートリポジトリにプッシュするには、git にユーザー情報を登録しておく必要があります（初回のみ）。

```bash
git config --global user.name "username"
git config --global user.email "e-mail@gmail.com"
```

## Usage

### Basic

-   **前回のコミットからの変更を表示**：`git status`
-   **インデックスにファイルの変更を登録**：`git add [登録したいファイル]`
-   **ローカルリポジトリに変更を記録**：`git commit -m "[メッセージ]"`
-   **リモートリポジトリに変更を同期**：`git push -u origin [ブランチ]`

### Branch

ブランチとは、**作業履歴を枝分かれさせて記録するためのもの**である。ブランチ上での変更は、統合されるまで他ブランチに影響しない。

-   **作成**：`git branch [名前]`
-   **一覧**：`git branch`
    -   `--all` リモート追跡ブランチも表示
    -   `HEAD` 現在のブランチの先頭（1 つ前`HEAD^`、2 つ前`HEAD^^`）
-   **切り替え**：`git checkout [ブランチ]`
    -   `-b` 作成と変更を同時に実行
-   **名前変更**：`git branch -m [元のブランチ] [新しいブランチ]`
-   **削除**：`git branch -d [ブランチ]`

### Remote Repository

-   **一覧**：`git remote`
    -   `-v` URL も表示
-   **追加**：`git remote add [リモート] [URL]`
-   **削除**：`git remote rm [リモート]`

### Tag

-   **作成**：`git tag [名前]`
-   **一覧**：`git tag`
-   **作成をリモートに反映**：`git push origin [タグ]`
-   **削除**：`git tag -d [タグ]`
-   **削除をリモートに反映**：`git push origin :[タグ]`

### Log

-   **コミット履歴**：`git log`
    -   `--merges` マージコミットだけ
    -   `--no-merges` マージコミット以外
    -   `--oneline`：一行で表示

### HEAD

-   **履歴一覧**：`git reflog`
-   **位置を変更**：

## Tips

### コミットメッセージ

-   [Git のコミットメッセージの書き方](https://qiita.com/itosho/items/9565c6ad2ffc24c09364)

### ブランチモデル

-   git-flow
-   GitHub Flow

## References

-   [サルでもわかる Git 入門](https://backlog.com/ja/git-tutorial/)
-   [いまさらだけど Git を基本から分かりやすくまとめてみた | Qiita](https://qiita.com/gold-kou/items/7f6a3b46e2781b0dd4a0)
