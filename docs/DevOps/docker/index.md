# Docker

Dockerは、コンテナ型仮想技術を実現する常駐アプリケーション（dockerd）と、それを操作するCLIからなるプロダクトです。

## インストール

=== "Mac / Windows"

    [公式サイト](https://www.docker.com/get-started)からDocker Desktopをダウンロードします。

=== "Linux"

    1. 必要なパッケージをインストールします。

        ```bash
        sudo apt-get update
        sudo apt-get install \
          apt-transport-https \
          ca-certificates \
          curl \
          gnupg-agent \
          software-properties-common
        ```

    2. Docker の公式 GPG キーを追加します。

        ```bash
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        ```

    3. Docker のaptリポジトリをstableリポジトリとして設定します。

        === "x86_64"

            ```bash
            sudo add-apt-repository \
                "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
                $(lsb_release -cs) \
                stable"
            ```

        === "armhf"

            ```bash
            sudo add-apt-repository \
                "deb [arch=amdhf] https://download.docker.com/linux/ubuntu \
                $(lsb_release -cs) \
                stable"
            ```

        === "arm64"

            ```bash
            sudo add-apt-repository \
                "deb [arch=arm64] https://download.docker.com/linux/ubuntu \
                $(lsb_release -cs) \
                stable"
            ```

    4. インストール

        ```bash
        sudo apt-get update
        sudo apt-get install docker-ce docker-ce-cli containerd.io
        ```

## 使い方

### `image build`

Dockerfileを元にイメージを作成します。

```bash
docker image build [OPTIONS] PATH
```

| オプション           | 説明                             |
| -------------------- | -------------------------------- |
| `-t イメージ[:タグ]` | イメージとタグ名。ほぼ必須       |
| `-f Dockerfile名`    | カスタムのDockerfile名を指定する |
| `--pull`             | ベースイメージを再取得する       |

### `image pull`

Docker Hubなどのレジストリから指定したイメージをダウンロードします。

```bash
docker image pull [OPTIONS] NAME[:TAG]
```

### `imgage ls`

Dockerホストにあるイメージの一覧を表示します。

```bash
docker image ls [OPTIONS] [REPOSITORY[:TAG]]
```

| オプション | 説明                 |
| ---------- | -------------------- |
| `-q`       | イメージIDだけを表示 |

### `image tag`

イメージの特定のバージョンにタグを付けます。

```bash
docker image tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```

### `image push`

イメージをDocker Hubなどのレジストリに登録・公開します。

```bash
docker image push [OPTIONS] NAME[:TAG]
```

### `image prune`

使用していないイメージを一括削除します。

```bash
docker image prune [OPTIONS]
```

### `container run`

イメージからコンテナを作成・実行します。

```bash
docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

| オプション          | 説明                                          |
| ------------------- | --------------------------------------------- |
| `-p HOST:CONTAINER` | HOSTからCONTAINERにポートフォワーディングする |
| `-d`                | コンテナをバックグランドで起動する            |
| `--name NAME`       | コンテナの名前                                |
| `-it`               | 標準入力と擬似端末を有効にする                |
| `--rm`              | コンテナ終了時にコンテナを破棄する            |
| `-v`                | ホストとコンテナ間でボリュームを共有する      |

### `container ls`

Dockerホストにあるコンテナの一覧を表示します。

```bash
docker container ls [OPTIONS]
```

| オプション        | 説明                           |
| ----------------- | ------------------------------ |
| `-q`              | コンテナIDだけを表示する       |
| `-a`              | 一覧に終了したコンテナも含める |
| `--filter filter` | 特定の条件でフィルタする       |

### `container stop`

実行中のコンテナを停止します。

```bash
docker container stop [OPTIONS] CONTAINER
```

### `container restart`

停止中のコンテナを再起動します。

```bash
docker container restart [OPTIONS] CONTAINER
```

### `container rm`

停止中のコンテナを削除します。

```bash
docker conainer rm [OPTIONS] CONTAINER
```

| オプション | 説明                             |
| ---------- | -------------------------------- |
| `-f`       | 実行中のコンテナを停止・削除する |

### `container logs`

実行中のコンテナの標準出力を表示します。

```bash
docker container logs [OPTIONS] CONTAINER
```

| オプション | 説明                   |
| ---------- | ---------------------- |
| `-f`       | 標準出力を取得し続ける |

### `contaienr exec`

実行中のコンテナで任意のコマンドを実行します。

```bash
docker container exec [OPTIONS] CONTAINER COMMAND [ARG...]
```

| オプション | 説明                           |
| ---------- | ------------------------------ |
| `-it`      | 標準入力と擬似端末を有効にする |

### `container cp`

ホスト・コンテナ間でファイル・ディレクトリをコピーします。

```bash
# コンテナからホストへコピー
dokcer container cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH

# ホストからコンテナへコピー
docker container cp [OPTIONS] SRC_PATH CONTAINER:DEST_PATH
```

### `container prune`

実行中でないコンテナを一括削除します。

```bash
docker container prune [OPTIONS]
```

### `container stats`

コンテナ単位でのシステムリソースの利用状況を取得します。

```bash
docker container stats [OPTIONS] [CONTAINER...]
```

### `version`

バージョン情報を取得します。

```bash
docker version
```

### `search`

Docker Hub等のレジストリに登録されているイメージを検索します。

```bash
docker serarch [OPTIONS] TERM
```

## 参考

- [docker docs](https://docs.docker.com/)
