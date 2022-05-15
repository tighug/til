# Solidity Usage

- [Solidity in Depth](https://solidity-jp.readthedocs.io/ja/latest/solidity-in-depth.html)

## File

### pragma

ファイルの一行目で、必ず利用するコンパイラのバージョンを指定する。

```js
pragma solidity [version];
```

### import

JavaScript（ES6）の様に、他のファイルを import できる。

```js
import "filename";
```

### comment

以下の他に、natspec 形式にも対応している。

```js
// one line
/* multiple lines */
```

## Structure of a Contract

### State Variables

状態変数。値が永久的にコントラクトのストレージに保存される。

```js
contract SimpleStorage {
    uint storedData; // State variable
}
```

### Functions

関数。`visibility`でアクセス制御を行う。

```js
function bid() public payable { // Function
// ...
}
```

### Function Modifiers

修飾子。主に Function のアクセス制御に用いる。

```js
modifier onlySeller() { // Modifier
        require(
            msg.sender == seller,
            "Only seller can call this."
        );
        _;
    }

    function abort() public view onlySeller { }
}
```

### Events

`event`で宣言、`emit`で発火。

```js
event HighestBidIncreased(address bidder, uint amount); // Event

function bid() public payable {
    emit HighestBidIncreased(msg.sender, msg.value); // Triggering event
}
```

### Struct Types

構造体。複数の変数をグループし、新しい型を宣言する。

```js
 struct Voter { // Struct
    uint weight;
    bool voted;
    address delegate;
    uint vote;
}
```

### Enum Types

有限個の`constant`な値を持つカスタムな型を宣言する。

```js
enum State { Created, Locked, Inactive } // Enum
```

## Types

### Value Types

#### Booleans

`bool`：`true`か`false`

#### Integers

`int` / `uint`：符号付き整数 / 符号なし整数

- `uint8`（`int8`）から`uint256`（`int256`）まで 8 ずつ上がる。
- `uint`と`int`はそれぞれ`uint256`と`int256`のエイリアス
- [切り捨て時の動作](https://solidity-jp.readthedocs.io/ja/latest/security-considerations.html#underflow-overflow)
- 整数の除算結果は整数：`int256(-5) / int256(2) == int256(-2)`
- 0 の除算・剰余演算は失敗する
- 符号なし整数のみ、指数演算（e.g.`2**10`）が利用できる

#### Fixed Point Numbers

使えない。

#### Address

`address`：20Byte の値
`address payable`：メンバ`transfer`と`send`が利用できる`address`

- メンバ
  - `balance`：残高
  - `transfer(val)`：`val`分 Ether を送る（単位は`wei`）
  - `send`：`transfer`の低レベルバージョン。非推奨

#### Contract Types

#### Fixed-size Bite Arrays

`byte1`、`byte2`...`byte32`：1 から 32 までの byte 配列

- `byte`は`byte1`のエイリアス
- メンバ
  - `.length`：固定長の byte 配列（readonly）

#### Dynamically-size Bite Array

`bytes`：動的サイズの byte 配列
`string`：動的サイズの UTF-8 の文字列

#### Rational and Integer Literals

0 から 9 までの数字で形成する

- 小数：`1.3`
- 指数：`2e10`

#### String Literals and Types

ダブルクォーテーション`""`で囲む

#### Hexadecimal Literals

接頭辞`hex`を付け、ダブルクォーテーション`""`で囲む

- `hex"001122FF"`

#### Enums

0 で始まる符号なし整数値によって表される（C 言語の列挙型と同じ）

#### Function Types

`internal`か`external`

```js
function (<parameter types>) {internal|external} [pure|view|payable] [returns (<return types>)]
```

### Reference Types

#### Data Location

Reference Type（参照型）では、関数内での宣言時に`memory`か`storage`かを明示する必要がある

- `memory`：書き換え時に、ローカル変数を参照する。コスト低
- `storage`：書き換え時に、状態変数を参照する。コスト高

#### Arrays

- メンバ
  - `length`：配列の大きさ
  - `push(val)`：配列の最後に要素`val`を追加
    - 戻り値として新しい配列の`length`を返す
  - `pop()`：配列の最後の要素を削除

#### Structs

構造体

### Mapping Types

`mapping(_KeyType => _ValueType)`

## Units

### Ether

- `1 wei == 1`
- `1 szabo == 1e12`
- `1 finney == 1e15`
- `1 ether == 1e18`

### Time

- `1 == 1 seconds`
- `1 minutes == 60 seconds`
- `1 hours == 60 minutes`
- `1 days == 24 hours`
- `1 weeks == 7 days`

## Special Variables & Functions

### Block and Transaction Properties

- `blockhash(uint blockNumber) returns (bytes32)`: 与えられたブロックのハッシュ
  - 現在のブロックを除いた直近 256 個のブロックのみで有効
- `block.coinbase (address payable)`: 現在のブロックのマイナーのアドレス
- `block.difficulty (uint)`: 現在のブロックの difficulty
- `block.gaslimit (uint)`: 現在のブロックのガスリミット
- `block.number (uint)`: 現在のブロックナンバー
- `block.timestamp (uint)`: 現在の unix のタイムスタンプ（秒）
- `gasleft() returns (uint256)`: 残ガス
- `msg.data (bytes calldata)`: コールデータ
- `msg.sender (address payable)`: メッセージの送信者
- `msg.sig (bytes4)`: コールデータの始め 4byte（例：ファンクションの識別子）
- `msg.value (uint)`: メッセージと一緒に送られた wei の量
- `now (uint)`: 現在のブロックのタイムスタンプ ( block.timestamp のエイリアス)
- `tx.gasprice (uint)`: トランザクションのガスプライス
- `tx.origin (address payable)`: トランザクションの送信者 (フルコールチェーン)

### Error Handling

- `assert(bool condition)`:
  - 条件を満たしていないと、invalid opcode を発生させ、その結果 state change reversion が起きます
  - 内部エラーに使用されます。
- `require(bool condition)`:
  - 条件を満たしていないと、revert します
  - 入力か外部要素に対してのエラーに使用されます。
- `require(bool condition, string memory message)`:
  - 条件を満たしていないと、revert します
  - 入力か外部要素に対してのエラーに使用されます。加えてエラーメッセージも出力されます。
- `revert()`:
  - 実行を中断し、state の変化を元に戻します。
- `revert(string memory reason)`:
  - 説明付きで実行を中断し、state の変化を元に戻します。

### Mathematical and Cryptographic Functions

- `addmod(uint x, uint y, uint k) returns (uint)`
- `mulmod(uint x, uint y, uint k) returns (uint)`
- `keccak256(bytes memory) returns (bytes32)`
- `sha256(bytes memory) returns (bytes32)`
- `ripemd160(bytes memory) returns (bytes20)`
- `ecrecover(bytes32 hash, uint8 v, bytes32 r, bytes32 s) returns (address)`

### Contract Related

- `this`
- `selfdestruct(address payable recipient)`

## Expressions and Control Structures

## Contracts

### Creating Contracts

### Visibility & Getters

関数には以下のいずれかを必ず指定する必要がある。状態変数には`external`を指定できない。

- `external`：コントラクト外部からのみ呼び出せる
- `public`：コントラクトの外部・内部から呼び出せる
- `internal`：コントラクト内部のみ呼び出せる（継承含む）
- `private`：コントラクト内部のみ呼び出せる（継承含まない）

#### Getter Functions

`public`の状態変数を宣言すると、コンパイラは自動で`external`な getter を生成する。
この状態変数は外部からは関数、内部からは状態変数と評価される。

```js
contract C {
    uint public data = 42;
}

contract Caller {
    C c = new C();
    function f() public view returns (uint) {
        return c.data();
    }
}
```

- `public`の Array 型の状態変数の場合、1 要素しか取り出せない
  - ガスコストを小さくする仕組み
  - 配列全体が欲しい場合は、それ用の関数を作る必要がある

### Function Modifier

`_;`の後に、元の関数の内容が実行される

### Constant State Variables

状態変数は`constant`で、固定値として宣言できる

### Function

#### Function Parameters and Return Variables

引数は JavaScript の様に、入力として受け付ける。
戻り値は JavaScript と違い、任意の数の値を出力できる。

```js
function arithmetic(uint _a, uint _b)
  public
  pure
  returns (uint o_sum, uint o_product)
{
  return (_a + _b, _a * _b);
}
```

#### View Functions

状態変数を変更しない場合、関数には`view`を宣言する。`getter`関数は自動で`view`が付く。
ただし、下記は状態変数を変更する。

- 状態変数を記述する
- イベントの発火`emit`
- 他のコントラクトを作る
- `selfdestruct`を使う
- call を通じて Ether を送る
- `view`や`pure`の付いていない関数を呼び出す
- 低レベル call を使う
- ある opcode の入ったインラインアセンブリを使う

#### Pure Functions

状態変数を変更せず、何も読まない場合、関数には`pure`を宣言する。
ただし、下記は状態変数を読む。

- 状態変数を読む。
- `address(this).balance` もしくは `<address>.balance` にアクセスする
- `block`、`tx`、`msg` ( `msg.sig` と `msg.data` は除く)のどれかにアクセスする
- `pure` が付いていない関数を呼び出す
- ある opcode の入ったインラインアセンブリを使う

#### Fallback Function

コントラクトは 1 つだけ名前のない関数を持つことができる。この関数は、引数も戻り値も持てず、visibility は`external`である必要がある。また、Ether を受け取るために`payable`である必要がある。関数を呼び出す際に、他の関数に当てはまらなかったり、何のデータも渡されなかった場合に実行される。

#### Function Overloading

コントラクトは異なるパラメータを持つ、同じ名前のファンクションを複数持つことができる。

```js
function f(uint _in) public pure returns (uint out) {
  out = _in;
}

function f(uint _in, bool _really) public pure returns (uint out) {
  if (_really)
    out = _in;
}
```

### Event

### Inheritance

#### Constructors

コンストラクタは `constructor` キーワードで宣言され、コントラクト生成時に実行される任意の関数で、コントラクトの初期化コードを実行できる。

```js
contract A {
  uint public a;

  constructor(uint _a) internal {
    a = _a;
  }
}

contract B is A(1) {
  constructor() public {}
}
```

### Abstract Contracts

### Interfaces

### Libraries

### Using For
