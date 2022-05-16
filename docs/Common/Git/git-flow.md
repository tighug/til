# git-flow

**git-flow** は、git のブランチモデルのひとつである。役割が決められた 5 種類のブランチを切り替えながら開発を行う。また、git-flow モデルをサポートするための、同名のコマンドツールでもある。

## Installation

=== "macOS"

    ```bash
    brew install git-flow
    ```

## Branches

### master

プロダクトとしてリリースするためのブランチ。直接コミットせずに、マージだけを行う。

### develop

開発の中心となるブランチ。直接コミットせずに、マージだけを行う。

### feature / \*

機能の追加や変更、バグフィックスを行うブランチ。ひとつの変更に対してひとつの feature ブランチを切る。develop ブランチから派生させて作業を開始する。作業完了後、再び develop ブランチにマージする。マージ後には削除する。

### release / \*

リリースの準備を行うブランチ。バージョンアップや、小さなバグ修正を行う。develop ブランチから派生させて作業を行う。作業完了後、develop ブランチと master ブランチにマージする。

### hotfix / \*

master ブランチの緊急のバグフィックスを行うブランチ。master ブランチから派生させて作業を開始する。作業完了後、develop ブランチと master ブランチにマージする。

## Workflow

### 1. ローカルリポジトリにクローンする

```bash
git clone https://github.com/tighug/[repo].git
```

### 2. git-flow を初期化する

```bash
git flow init
```

### 3. feature ブランチで開発作業を行う

ブランチを切る。名前は「1-set-up-repo」のような作業内容を付ける。対応する issue がある場合には、名前の最初に番号を付ける。

```bash
git flow feature start [name]
```

開発作業を完了する。

```bash
git flow feature finish [name]
```

### 4. release ブランチでリリース準備を行う

ブランチを切る。名前には 1.0 のようなバージョン番号を付ける。バージョン番号は semver に従う。

```bash
git flow release start [name]
```

ブランチ内でバージョンアップ作業を行う。

```bash
yarn version --no-git-tag-version
```

ブランチ内で適宜小さなバグフィックスを行い、release ブランチでの作業を完了する。

```bash
git flow release finish [name]
```

### 5.（hotfix ブランチで緊急のバグフィックスを行う）

ブランチを切る。

```bash
git glow hotfix start [name]
```

作業を完了する。

```bash
git glow hotfix finish [name]
```

## References

-   [Git-flow って何？](https://qiita.com/KosukeSone/items/514dd24828b485c69a05)
-   [Git-flow ～ Git のブランチモデルを知る～](https://tracpath.com/bootcamp/learning_git_git_flow.html)
-   [nvie/gitflow | GitHub](https://github.com/nvie/gitflow)
