# Compose

Composeは、複数コンテナから構成されるサービスを管理するツールです。

## インストール

=== "Windows / Mac"

    Docker Desktopをインストールする。

=== "Ubuntu"

    1. Composeの最新版をダウンロードします。

        ```bash
        sudo curl -L https://github.com/docker/compose/releases/download/1.27.4/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
        ```

    2. バイナリに対して実行権限を付与します。

        ```bash
        sudo chmod +x /usr/local/bin/docker-compose
        ```

## 使い方

### `build`

サービスをイメージからビルドします。

```bash
docker-compose build [OPTIONS] [SERVICE...]
```

### `create`

サービスを作成します。

```bash
docker-compose build [OPTIONS] [SERVICE...]
```

### `start`

サービスを実行します。

```bash
docker-compose start
```

### `up`

サービスを作成・実行します。

```bash
docker-compose up [OPTIONS] [SERVICE...]
```

| オプション | 説明                               |
| ---------- | ---------------------------------- |
| `-d`       | サービスをバックグランドで起動する |

### `stop`

実行中のサービスを停止します。

```bash
docker-compose stop [OPTIONS] [SERVICE...]
```

### `rm`

実行中のサービスを停止する。

```bash
docker-compose rm [OPTIONS] [SERVICE...]
```

### `down`

実行中のサービスを停止・削除します。

```bash
docker-compsoe down [OPTIONS]
```

### `ps`

実行中のサービス一覧を表示します。

```bash
docker-compose ps [OPTIONS] [SERVICE...]
```

### `logs`

実行中のサービスの標準出力を表示します。

```bash
docker-compose logs [OPTIONS] [SERVICE...]
```

## 設定

`docker-compose.yml`に記述します。

### 全体

| name     | description                                                  |
| -------- | ------------------------------------------------------------ |
| version  | 使用するバージョン                                           |
| services | アプリを動かす要素                                           |
| volumes  | マウントするボリュームのパス（Host : Container）             |
| network  | デフォルトのネットワークの代わりに、任意のネットワークを指定 |

### services

| name    | description                                      |
| ------- | ------------------------------------------------ |
| image   | イメージの名前                                   |
| build   | `Dockerfile`のあるディレクトリのパスを指定する。 |
| command | デフォルトのコマンドを上書きする。               |
| links   | 他のコンテナにリンクする。                       |
| ports   | 公開（EXPOSE）するポート。                       |
| volumes | マウントするボリュームのパス。                   |

## 参考

- [docker docs](https://docs.docker.com/)
