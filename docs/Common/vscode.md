# VSCode

VSCode とは、**Microssoft が開発したオープンソースのテキストエディタ**です。拡張機能が便利で、統合ターミナルが使えます。必要な言語だけ拡張機能で追加できるので、UI や機能も最低限で済みます。

-   [Visual Studio Code のインストールと使い方](https://eng-entrance.com/texteditor-vscode)
-   [VSCode + WSL](https://qiita.com/remin/items/b764036e95a13075ee98)

## Installation

[Visual Studio Code の公式サイト](https://code.visualstudio.com/)からダウンロードします。

## Shortcuts

-   [Windows 版](https://qiita.com/TakahiRoyte/items/cdab6fca64da386a690b)
-   [Mac 版](https://qiita.com/naru0504/items/99495c4482cd158ddca8)

## Extensions

### Utility

| Extensions             | Description                            |
| ---------------------- | -------------------------------------- |
| Japanese Language Pack | 日本語化                               |
| Better Comments        | TODO コメントのハイライト              |
| Bracket Pair Colorizer | 括弧の対応を色付きで表示してくれる     |
| GitLens                | Git 機能の拡張                         |
| Log File Highlighter   | Log ファイルのハイライト               |
| Output Colorizer       | Output のハイライト                    |
| Setting Sync           | ユーザー設定等を複数 PC 間で同期可能に |
| Todo Tree              | TODO コメントの機能拡張                |
| zenkaku                | コード内の全角の空白を表示             |

### Front-end / Back-end

| Extensions                    | Description                   |
| ----------------------------- | ----------------------------- |
| npm                           | npm サポート                  |
| npm Intellisense              | npm 入力補完                  |
| ESLint                        | JavaScript の Linter          |
| Prettier                      | Code formatter                |
| Auto Rename Tag               | HTML タグを自動で Rename する |
| Auto Close Tag                | HTML タグを自動で閉じる       |
| JavaScript(ES6) code snippets | ES&コードスニペット           |
| Vetur                         | Vue の入力補完                |
| Vue 2 Snippets                | Vue2 のスニペット             |
| Vue Peek                      | Vue の定義移動・参照          |

### DevOps

| Extensions              | Description           |
| ----------------------- | --------------------- |
| Docker                  | Docker サポート       |
| Better TOML             | TOML 言語サポート     |
| EditorConfig for VSCode | EditorConfig サポート |
| DotENV                  | .env サポート         |

### Markdown

| Extensions                | Description                    |
| ------------------------- | ------------------------------ |
| Markdown Alii in One      | 機能拡張                       |
| Markdown Preview Enhanced | プレビューをカスタマイズ可能に |
| markdownlint              | リンター                       |
| Paste Image               | 画像の貼り付け                 |

### Solidity

| Extensions | Description       |
| ---------- | ----------------- |
| solidity   | Solidity 言語対応 |

### CSV

| Extensions  | Description    |
| ----------- | -------------- |
| Rainbow CSV | CSV ハイライト |

### Theme

-   Atom One Dark Theme
-   Dracura Official
-   One Dark Pro
-   Panda Theme
-   Sublime Material Theme
-   SynthWave '84
-   Material Icon Theme

## Tips

### ターミナルを WSL に変更する

```JSON title="settings.json"
{
    "terminal.integrated.shell.windows": "C:/Windows/System32/wsl.exe"
}
```

### WSL で Git を使う

1. [WSLGit](https://github.com/andy-5/wslgit)のバイナリ`wslgit.exe`をダウンロードし、適当なディレクトリに移動。
2. パスを設定

```JSON title="settings.json"
{
    "git.path": "C:/bin/wslgit.exe"
}
```
