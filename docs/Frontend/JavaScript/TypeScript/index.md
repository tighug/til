# TypeScript

TypeScript は**Alt JavaScript 言語**です。コンパイルすることで JavaScript を生成します。

## Installation

```bash
yarn add -D typescript
```

## CLI

```bash
tsc [file]  # Transpile

tsc --init  # Initialize and create a tsconfig.json
```

## Configuration

`tsconfig.json`に記述します。

```json
{
  "compilerOptions": {
    // #### プロジェクト設定 ####
    // 出力する.jsファイルのバージョン
    "target": "ES3",
    // 出力するjsモジュールの仕組みに何を使用するか
    "module": "CommonJS",
    // .jsファイルをインポート可能にする
    "allowJs": false,
    // .jsファイル内のエラーを報告する（"allowJs"と併用）
    "checkJs": false,
    // .tsxファイルをどのように扱うか
    "jsx": "react",
    // .d.tsファイルを生成する
    "declaration": false,
    // .tsファイルに.d.tsファイルをマップする
    "declarationMap": false,
    // 古いバージョンのJavaScriptのイテレーションに対応する
    "downlevelIteration": false,
    // ダウンレベルする際、モジュール毎にコードを挿入せず、ライブラリからインポートして重複を避ける
    "importHelpers": false,
    // すべての.tsファイルを他隠逸のモジュールとしてコンパイルする
    "isolatedModules": false,

    // targetで指定したバージョン以外のライブラリを使用する
    "lib": ["ESNext"],
    // TypeScriptを型チェックツールとしてのみ使用する
    "noEmit": false,
    // トランスパイル結果を出力するディレクトリ
    "outDir": "dist",
    // トランスパイル結果を一つのファイルにまとめる（moduleがSystem/AMDの時のみ使用可）
    "outFile": "./dist/bundle.js",
    // エディタ内で動作させるLanguage Serviceのプラグイン
    "plugins": [],
    // コメントを消去する
    "removeComments": false,
    // 出力する際に、ツリー構造のルートとするディレクトリ
    "rootDir": ".",
    // 出力された.jsファイルから元の.tsファイルへのマップファイルを生成する
    "sourceMap": false,

    // ***
    "composite": false,
    // ***
    "incremental": false,
    // a
    "tsBuildInfoFile": ".tsbuildinfo",

    // #### 厳密なチェック ####
    // 以下の厳密なチェックルールすべてを有効にする
    "strict": false,
    // "use strict"をファイルの先頭行に必ず追加する
    "alwaysStrict": false,
    // 暗黙的なany型をエラーにする
    "noImplicitAny": false,
    // 暗黙的なany型となるthis変数をエラーにする
    "noImplicitThis": false,
    // strict/call/applyの使用時に、厳密な型チェックを行う
    "strictBindCallApply": false,
    // 関数の引数に、厳密な型チェックを行う
    "strictFunctionTypes": false,
    // nulllableな変数に、厳密な型チェックを行う
    "strictNullChecks": false,
    // クラスのプロパティに、厳密な型チェックを行う
    "strictPropertyInitialization": false,

    // #### モジュール解決 ####
    // ルートとなるディレクトリ
    "baseUrl": "./",
    // インポート時の長い相対パスを避けるために、baseUrlからの相対的な場所に再マッピングする
    "paths": {
      "app/*": ["app/*"]
    },
    // すべてのインポートに対してNamespaceオブジェクトを生成する
    "esModuleInterop": false,
    "allowSyntheticDefaultImports": false,
    "allowUmdGlobalAccess": false,
    // モジュール解決の方法（moduleで自動で設定されるので、ほとんどの場合は必要ない）
    "moduleResolution": "",
    // シンボリックリンクを実体パスへ解決しない
    "preserveSymlinks": false,
    // 単一のルートとして振る舞う仮想的な複数のディレクトリを設定する
    "rootDirs": [],
    // インクルードするパッケージのディレクトリ
    "typeRoots": [],
    // インクルードするパッケージ
    "types": [],

    // #### ソースマップ ####
    // ソースマップを.js.mapファイルへ出力せずに、.jsファイルに埋め込む（sourceMapとは排他的）
    "inlineSourceMap": false,
    // 元の.tsファイルの内容をソースマップに埋め込む
    "inlinseSource": false,
    // デバッガがマップファイルを探索すべき場所
    "mapRoot": "",
    // デバッガがソースコードを探索すべき場所
    "sourceRoot": "",

    // #### リンターチェック ####
    "noFallthroughCasesInSwitch": false,
    "noImplicetOverride": false,
    "noImplicitReturns": false,
    "noPropertyAccessFromIndexSignature": false,
    "noUncheckedIndexedAccess": false,
    "noUnusedLocals": false,
    "noUnusedParameters": false
  },
  // トランパイル対象のファイル。ファイルが少数の時に有用
  "files": ["core.ts"],
  // 継承したい別のtsconfig.jsonの場所
  "extends": "./configs/base",
  // トランスパイル対象のファイル
  "include": ["src/**/*", "tests/**/*"],
  // includeの解決時に除外するファイル
  "exclude": [],
  "references": [{ "path": "../src" }]
}
```

## 型定義ファイル`.d.ts`

外部モジュールのインポート時に、エラーが出る場合。これは、そのモジュールが TypeScipt で利用されることを想定しておらず、TypeScript 用の型定義ファイルが不足しているからである。以下で型定義ファイルをインストールするか、`require`を使うことでエラーを解消できる。

```bash
yarn add -D @types/[moduleName]
```

## References

- [TypeScript tsconfig](https://www.typescriptlang.org/ja/tsconfig)
- [tsconfig.json の全オプションを理解する | Qiita](https://qiita.com/ryokkkke/items/390647a7c26933940470#outfile)
