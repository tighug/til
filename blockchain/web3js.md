# web3.js

- [web3.js - Ethereum JavaScript API](https://web3js.readthedocs.io/en/v1.2.4/)

## Installation

```bash
yarn add web3
```

## Web3

| api                       | returns            | description                        |
| ------------------------- | ------------------ | ---------------------------------- |
| `setProvider([provider])` | `boolean`          | プロバイダを変更                   |
| `givenProvider`           | `Object` or `null` | ブラウザで設定されているプロバイダ |
| `currentProvider`         | `Object` or `null` | 現在のプロバイダ                   |

### インスタンス化

```js
import Web3 from "web3";

const web3 = new Web3(Web3.givenProvider || "http://localhost:8545");
```

## web3.eth

| api                   | returns            | description                      |
| --------------------- | ------------------ | -------------------------------- |
| `isMining()`          | `Promise<boolean>` | マイニング中か                   |
| `getHashrate()`       | `Promise<Number>`  | ハッシュレート                   |
| `getGasPrice()`       | `Promise<String>`  | ガスプライス（wei）              |
| `getAccounts()`       | `Promise<Array>`   | ノードが制御するアカウントリスト |
| `getBlockNumber(])`   | `Promise<Number>`  | 現在のブロック数                 |
| `getBalance(address)` | `Promise<String>`  | `address`のアカウントの残高      |
| `getBlock(blockNum)`  | `Promise<Object>`  | `blockNum`のブロック情報         |

### net

| api              | returns           | description        |
| ---------------- | ----------------- | ------------------ |
| `getId()`        | `Promise<Number>` | ネットワーク ID    |
| `getPeerCount()` | `Promise<Number>` | ピア数             |
| `getNetworkType` | `Promise<String>` | ネットワークタイプ |

### subscribe

### Contract

- `new web3.eth.Contract(jsonInterface)`

### accounts

### personal

- `newAccount(password)`
- `unlockAccount(address, password, unlockDuraction)`
