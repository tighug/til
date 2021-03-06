# Prettier

Prettierはコードフォーマッターのひとつです。

以下のプログラミング言語に対応しています。

- JavaScript
- JSX
- Angular
- Vue
- Flow
- TypeScript
- CSS/Less/SCSS
- HTML
- JSON
- GraphQL
- Markdown（GFMとMDXを含む）
- YAML

## インストール

=== "yarn"

    ```bash
    yarn add -D prettier
    ```

=== "npm"

    ```bash
    npm install -D prettier
    ```

## 使い方

=== "yarn"

    ```bash
    yarn prettier --write .
    ```

=== "npm"

    ```bash
    npx prettier --write .
    ```

## 設定

`.prettierrc.yml`に記述します。

```yaml
# .prettierrc.yml（値はデフォルト）
printWidth: 80  # 一行の長さ
tabWidth: 2     # タブ幅
useTabs: false  # インデントにスペースの代わりにタブを使う
semi: true      # ステートメントの最後にセミコロンを記述する
singleQuote: false  # 二重引用符の代わりに単一引用符を使う
quoteProps: "as-needed" # オブジェクトのプロパティに引用符を付ける
jsxSingleQuote: false   # JSXの場合、二重引用符の代わりに単一引用符を使う
trailingComma: "es5"    # 複数行の場合、末尾にコンマを記述する
bracketSpacing: true    # オブジェクトリテラルの括弧の間にスペースを入れる
jsxBracketSameLine: false   # JSXの括弧を最後の行の末尾に置く
arrowParens: "always"   # アロー関数の引数を括弧で囲む
rangeStart: 0           # フォーマット範囲（始まりの文字数）
rangeEnd:  Infinity     # フォーマット範囲（終わりの文字数）
parser:  ""             # 使用するパーサー
proseWrap: "preserve"   # 文章を折り返す
htmlWhitespaceSensitivity: "css"    # HTMLファイルの空白の感度
vueIndentScriptAndStyle: false      # Vueファイルの<script>と<style>タグをインデントする
endOfLine: "lf"         # 行末文字
embeddedLanguageFormatting: "auto"  # 引用コードをフォーマットする
```

??? note "設定ファイルの形式"

    以下の形式に対応しています。

    - `package.json`ファイル内のprettierキー
    - JSONもしくはYAMLで書かれた`.prettierrc`ファイル
    - `.prettierrc.json`、`.prettierrc.yml`、`.prettierrc.yaml`、`.prettierrc.json5`
    - `.prettierrc.js`、`prettierrc.cjs`、`prettier.config.js`、`prettier.config.cjs`
    - `.prettierrc.toml`

Prettierによるフォーマットを適応したくないファイルは、`.prettierignore`に記述します。

## 参考

- [Prettier](https://prettier.io/docs/en/index.html)
