# ERC 20

最も広く使われている代替可能トークン（FT：Fungible Token）。

## IERC20

EIP で定義されている ERC20 標準のインターフェース。

| method                                                            | return  | description                                                                                                                                                 |
| ----------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `totalSupply()`                                                   | uint256 | 存在するトークンの量                                                                                                                                        |
| `balanceOf(address account)`                                      | uint256 | `account`が所有するトークンの量                                                                                                                             |
| `transfer(address recipient, uint256 amount)`                     | bool    | `amount`分のトークンを呼び出し元から recipient に送る                                                                                                       |
| `allowance(address owner, address spender)`                       | uint256 | `transferFrom`を使用して spender が利用できる owner のトークンの量 (デフォルトで 0)                                                                         |
| `approve(address spender, uint256 amount)`※                       | bool    | 呼び出し元の`amount`分のトークンに利用を`spender`に許可する                                                                                                 |
| `transferFrom(address sender, address recipient, uint256 amount)` | bool    | `sender`から`recipient`に`amount`分のトークンを送る。`amount`は呼び出し元の`allowance`以下でなければならない。送られると`allowance`が`amount`分差し引かれる |

※ approve
この方法で許容値を変更すると、不幸なトランザクションの順序付けにより、誰かが古い許容値と新しい許容値の両方を使用するリスクが生じる。この競合状態を緩和するための 1 つの解決策は、最初に支出者の手当を 0 に減らし、その後で希望の値を設定すること。（[参照](https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729)）

| event                                                     | description                                      |
| --------------------------------------------------------- | ------------------------------------------------ |
| `Transfer(address from, address to, uint256 value)`       | `transfer`・`transferFrom`が呼ばれると発火される |
| `Approval(address owner, address spender, uint256 value)` | `approve`が呼ばれると発火される                  |

## ERC20

IERC20 の実装。

| method                                                         | return | description                                                                            |
| -------------------------------------------------------------- | ------ | -------------------------------------------------------------------------------------- |
| IERC20 の全関数                                                | -      | IERC の関数参照（ただし、external→public）                                             |
| `increaseAllowance(address spender, uint256 addedValue)`       | bool   | `speder`が利用できるトークンの量を addedValue 分だけ増やす                             |
| `decreaseAllowance(address spender, uint256 subtractedValue)`  | bool   | `speder`が利用できるトークンの量を`addedValue`分だけ増やす                             |
| `_transfer(address sender, address recipient, uint256 amount)` | void   | `transfer`の内部関数                                                                   |
| `_mint(address account, uint256 amount)`                       | void   | `amount`分トークンを作成し、`account`に割り当てる                                      |
| `_burn(address account, uint256 value)`                        | void   | `account`の`amount`分のトークンを破壊する                                              |
| `_approve(address owner, address spender, uint256 value)`      | void   | `approve`の内部関数                                                                    |
| `_burnFrom(address account, uint256 amount)`                   | void   | `account`の`amount`分のトークンを破壊する。破壊後、`allowance`が`amount`分差し引かれる |

## ERC20Detailed

| method                                                    | return | description                                                                      |
| --------------------------------------------------------- | ------ | -------------------------------------------------------------------------------- |
| ERC20 の全関数                                            | -      | ERC の関数参照                                                                   |
| `constructor(string name, string symbol, uint8 decimals)` | void   | `name`・`symbol`・`decimals`を設定する。構築時に一度だけ呼ばれる。3 つの値は不変 |
| `name()`                                                  | string | トークンの名前                                                                   |
| `symbol()`                                                | string | トークンのシンボル                                                               |
| `decimals()`                                              | uint8  | 小数の数（e.g. decimals=2 の時、505→5.05）                                       |

## ERC20Mintable（Extentions）

| method                                  | return | description           |
| --------------------------------------- | ------ | --------------------- |
| `mint(address account, uint256 amount)` | bool   | `_mint`の public 関数 |

## ERC20Burnable（Extentions）

| method                                      | return | description               |
| ------------------------------------------- | ------ | ------------------------- |
| `burn(uint256 amount)`                      | void   | `_burn`の public 関数     |
| `burnFrom(address account, uint256 amount)` | void   | `_burnFrom`の public 関数 |

## ERC20Pausable（Extentions）

送金時に一時停止が可能になる。

## ERC20Capped（Extentions）

Mintable のトークン生成に上限が設定できる。

## SafeERC20（Utility）

関数実行失敗時にスローされる ERC20 のラッパー。

```js
using SafeERC20 for ERC20;
```
