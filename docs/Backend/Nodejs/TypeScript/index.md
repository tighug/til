# TypeScript

TypeScript とは、**静的型付きプログラミング言語であり、Alt JavaScript 言語の 1 つ**です。コンパイルすることで JavaScript が生成されます。

## Installation

=== "Yarn"

    ```bash
    yarn add -D typescript
    ```

=== "NPM"

    ```bash
    npm install -D typescript
    ```

## CLI

```bash
tsc [file]  # Transpile

tsc --init  # Initialize and create a tsconfig.json
```

## Configuration

Ref : [TypeScript tsconfig](https://www.typescriptlang.org/v2/en/tsconfig)

`tsconfig.json`に記述します。

### `include`

トランスパイル対象のファイル

### `exclude`

トランスパイル対象から除外するファイル

### `compilerOptions`

| options        | default             | description                                       |
| -------------- | ------------------- | ------------------------------------------------- |
| target         | "ES3"               | トランスパイル後の ECMA のバージョン              |
| module         | "CommonJS" or "ES6" | 出力するモジュールの仕組み                        |
| allowJs        | false               | JavaScript をコンパイルできるようにする           |
| checkJs        | false               | JS のエラーも指摘する。「allowJs」と併用          |
| jsx            | preserve            | JSX ファイルをどのようにエミットするか（"react"） |
| declaration    | true when TS        | プロジェクト内の各ファイルの d.ts を生成する      |
| declarationMap | false               | d.ts のソースマップを生成する                     |
| sourceMap      | false               | デバッガーに.js ではなく.ts を参照させる          |
| outDir         | n/a                 | トランスパイル後にエミットするディレクトリ        |
| noEmit         | false               | エミットしない                                    |

#### Strict Type-Checking Options

- `strict` / `false` : 厳密なチェックオプションを全て有効にする

#### Module Resolution Options

- `esModuleInterop` / `false` : CommonJS と ES モジュールの相互運用を可能にする
- `allowSyntheticDefaultImports` / `false` : import/export の互換性を緩める
- `resolveJsonModule` / `false` : JSON のインポートを許可する

## Configuration Example

```json
{
  "compilerOptions": {
    "strict": true,
    "sourceMap": true,
    "target": "ES6", // ES5かES6
    "module": "Commonjs", // targetがES5ならCommonjs、ES6ならES6
    "moduleResolution": "Node" // NodejsならNode、BrowserならClassic
  },
  // コンパイル対象
  "include": ["src/**/*"],
  // コンパイル対象から除外
  "exclude": ["node_modules", "**/*.spec.ts"]
}
```

## 型定義ファイル`.d.ts`

外部モジュールのインポート時に、エラーが出る場合。これは、そのモジュールが TypeScipt で利用されることを想定しておらず、TypeScript 用の型定義ファイルが不足しているからである。以下で型定義ファイルをインストールするか、`require`を使うことでエラーを解消できる。

```bash
yarn add -D @types/[moduleName]
```
