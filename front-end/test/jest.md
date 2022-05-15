# Jest

Jest は JavaScript のテスティングフレームワークです。

## Installation

```bash
yarn add -D jest
yarn add -D ts-jest @types/jest # For TypeScript
```

## CLI

```bash
jest # すべてのテストを実行する
jest [file] # 指定されたテストのみ実行する
```

| options                 | description                                |
| ----------------------- | ------------------------------------------ |
| `--ci`                  | CI 環境を仮定して実行する                  |
| `--coverage`            | カバレッジを出力する                       |
| `--init`                | `jest.config.js`を生成する                 |
| `--updateSnapshot`/`-u` | スナップショットを更新する                 |
| `--watch`               | ファイル変更時にテストを再実行する         |
| `--watchAll`            | ファイル変更時にすべてのテストを再実行する |

## Configuration

`jest.config.js`に記述します。

```js
module.exports = (request, options) => {
  testMatch: [
    "**/__tests__/**/*.[jt]s?(x)",
    "**/?(*.)+(spec|test).[jt]s?(x)"
  ], // （デフォルト）テストファイルのglobパターン
};
```

| options            | default | description                  |
| ------------------ | ------- | ---------------------------- |
| `testEnvinronment` | `jsdom` | テスト環境（`node`/`jsdom`） |

## API

### Globals

| methods                   | description                                        |
| ------------------------- | -------------------------------------------------- |
| `afterAll(fn, timeout)`   | ファイル内の最後のテストが完了した後に関数を実行   |
| `afterEach(fn, timeout)`  | ファイル内の各テストが完了した後に関数を実行       |
| `beforeAll(fn, timeout)`  | ファイル内の最初のテストが実行される前に関数を実行 |
| `beforeEach(fn, timeout)` | ファイル内の各テストが実行される前に関数を実行     |

| methods                   | description                          |
| ------------------------- | ------------------------------------ |
| `describe(name, fn)`      | 関連するテストまとめたブロックを作成 |
| `test(name, fn, timeout)` | テストを実行                         |

### Expect

| methods                 | description                         |
| ----------------------- | ----------------------------------- |
| `toBe(value)`           | 同値                                |
| `not`                   | 否定                                |
| `toBeFalsy()`           | `false`/`null`/`undefined`/`0`/`""` |
| `toBeTruthy()`          | 上記の逆                            |
| `toBeNull()`            | `null`                              |
| `toBeUndefined()`       | `undefined`                         |
| `toBeDefined()`         | 上記の逆                            |
| `toBeInstanceOf(Class)` | あるクラスのインスタンス            |

#### 文字列

| methods           | description  |
| ----------------- | ------------ |
| `toMatch(reqexp)` | ある正規表現 |

#### 数値

| methods                          | description        |
| -------------------------------- | ------------------ |
| `toBeNaN()`                      | `NaN`              |
| `toBeGreaterThan(number)`        | ある数字より大きい |
| `toBeGreaterThanOrEqual(number)` | ある数字以上       |
| `toBeLessThan(number)`           | ある数字より小さい |
| `toBeGreaterThanOrEqual(number)` | ある数字以下       |
| `toHaveLength(number)`           | ある数字の長さ     |

#### 配列

| methods           | description                    |
| ----------------- | ------------------------------ |
| `toContain(item)` | 配列内に特定の値が含まれている |

#### 例外

| methods           | description |
| ----------------- | ----------- |
| `toThrow(error?)` | 例外        |

### Mock Functions

| methods              | description |
| -------------------- | ----------- |
| `describe(name, fn)` |             |

## References

- [Jest](https://jestjs.io/ja/)
