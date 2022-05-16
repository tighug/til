# ERC 777

ERC20 の欠点を補うように考えられた代替可能トークン（FT：Fungible Token）。ERC20 とは下位互換性を持つ。

## IERC777

| method                                                                                            | return    | description                                                                                                      |
| ------------------------------------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| `name()`                                                                                          | string    | トークンの名前                                                                                                   |
| `symbol()`                                                                                        | string    | トークンのシンボル。通常は名前の短縮バージョン                                                                   |
| `grabularity()`                                                                                   | uint256   | トークンの割り切れない最小数。すべてのトークン操作（`mint`, `send`, `burn`）がこの倍数である必要がある。通常は 1 |
| `totalSupply()`                                                                                   | uint256   | 存在するトークンの量                                                                                             |
| `balanceOf(address owner)`                                                                        | uint256   | `owner`が所有するトークンの量                                                                                    |
| `send(address recipient, uint256 amount, bytes data)`                                             | void      | `amount`分のトークンを呼び出し元から`recipient`に送る                                                            |
| `burn(uint256 amount, bytes data)`                                                                | void      | `account`の`amount`分のトークンを破壊する                                                                        |
| `isOperatorFor(address operator, address tokenHolder)`                                            | bool      | `operator`が`tokenHolder`のオペレータであるか。（すべてのアカウントは自身のオペレータ）                          |
| `authorizeOperator(address operator)`                                                             | void      | `operator`を呼び出し元のオペレータにする                                                                         |
| `revokeOperator(address operator)`                                                                | void      | `operator`を呼び出し元のオペレータから外す                                                                       |
| `defaultOperators()`                                                                              | address[] | デフォルトのオペレータのリストを返す                                                                             |
| `operatorSend(address sender, address recipient, uint256 amount, bytes data, bytes operatorData)` | void      | `amount`分のトークンを`sender`から`recipient`に送る                                                              |
| `operatorBurn(address account, uint256 amount, bytes data, bytes operatorData)`                   | void      | `account`から`amount`分のトークンを破棄する                                                                      |

| event                                                                                              | description                                              |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| `Sent(address operator, address from, address to, uint256 amount, bytes data, bytes operatorData)` | `send`・`operatorSend`・`transfer`が呼ばれると発火される |
| `Minted(address operator, address to, uint256 amount, bytes data, bytes operatorData)`             |                                                          |
| `Burned(address operator, address from, uint256 amount, bytes data, bytes operatorData)`           |                                                          |
| `AuthorizedOperator(address operator, address tokenHolder)`                                        |                                                          |
| `RevokeOperator(address operator, address tokenHolder)`                                            |                                                          |

## ERC777

IERC777 の実装。

| method                                                                                         | return  | description                                |
| ---------------------------------------------------------------------------------------------- | ------- | ------------------------------------------ |
| IERC777 の全関数                                                                               | -       | IERC の関数参照（ただし、external→public） |
| `transfer(address recipient, uint256 amount)`                                                  | bool    | IERC20.transfer                            |
| `allowance(address holder, address spender)`                                                   | uint256 | IERC20.allowance                           |
| `approve(address spender, uint256 value)`                                                      | bool    | IERC20.approve                             |
| `transferFrom(address holder, address recipient, uint256 amount)`                              | bool    | IERC20.transferFrom                        |
| `_mint(address operator, address account, uint256 amount, bytes userData, bytes operatorData)` | void    | mint の内部関数                            |

## IERC777Sender

| method                                                                                                       | return | description                                                      |
| ------------------------------------------------------------------------------------------------------------ | ------ | ---------------------------------------------------------------- |
| tokensToSend(address operator, address from, address to, uint256 amount, bytes userData, bytes operatorData) | void   | 登録済みアカウント**から**トークンが移動・破棄する直前に呼ばれる |

## IERC777Recipient

| method                                                                                                         | return | description                                                    |
| -------------------------------------------------------------------------------------------------------------- | ------ | -------------------------------------------------------------- |
| tokensReceived(address operator, address from, address to, uint256 amount, bytes userData, bytes operatorData) | void   | 登録済みアカウント**に**トークンが移動・生成する直前に呼ばれる |
