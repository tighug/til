# Ownable

State Variables

| variable | type      | type visibility | description      |
| -------- | --------- | --------------- | ---------------- |
| `_owner` | `address` | `private`       | 所有者のアドレス |

Modifiers

| modifier      | description              |
| ------------- | ------------------------ |
| `onlyOwner()` | 現在の所有者のみ実行可能 |

Functions

| function                               | return    | visibility         | description      |
| -------------------------------------- | --------- | ------------------ | ---------------- |
| `constructor()`                        | `void`    | `internal`         | コンストラクタ   |
| `owner()`                              | `address` | `public view`      | 現在の所有者     |
| `isOwner()`                            | `bool`    | `public view`      | 自身は所有者か   |
| `renounceOwnership()`                  | `void`    | `public onlyOwner` | 所有権を放棄する |
| `transferOwnership(address newOwner)`  | `void`    | `public onlyOwner` | 所有権を移行する |
| `_transferOwnership(address newOwner)` | `void`    | `internal`         | 所有権を移行する |

Events

| event                                                                           | description                  |
| ------------------------------------------------------------------------------- | ---------------------------- |
| `OwnershipTransferred(address indexed previousOwner, address indexed newOwner)` | 所有権が移行した時発火される |
