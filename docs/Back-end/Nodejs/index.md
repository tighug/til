# Node.js

Nodejs とは、**JavaScript をサーバーサイドで使えるようにしたもの**です。

-   [npm 入門（Qiita）](https://qiita.com/maitake9116/items/7825d90c09f3e2f87dea)

## Installation

=== "macOS"

    「nodebrew」をインストール

    ```bash
    brew install nodebrew
    ```

    Nodejs をインストール。同時に NPM もインストールされる

    ```bash
    nodebrew install-binary latest
    ```

    使用するバージョンの指定

    ```bash
    nodebrew use v7.1.0
    ```

=== "Linux"

    ```bash
    curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    sudo apt-get install -y nodejs
    ```

#### nodejs のアップデート

```bash
nodebrew ls
nodebrew install-binary latest
nodebrew use latest
```
