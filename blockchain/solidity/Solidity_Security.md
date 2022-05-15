# Solidity Security

- [Security Considerations](https://solidity-jp.readthedocs.io/ja/latest/security-considerations.html)

## Pitfalls

### Private Information and Randomness

- スマートコントラクト内の**全てはパブリックに見ることができる**
- ローカル変数でも`private`の状態変数でも

### Re-Entrancy

再入場。コントラクト A からコントラクト B にインタラクト及び送金をする時、コントラクト B がコントロール権利を持つ。このため、コードが実行完了前に A の関数を呼び出すことができる。
Re-Entrancy を回避するために、**Checks-Effects-Interactions**パターンを用いる

Bad

```js
// THIS CONTRACT CONTAINS A BUG - DO NOT USE
contract Fund {
  /// Mapping of ether shares of the contract.
  mapping(address => uint) shares;
  /// Withdraw your share.
  function withdraw() public {
    if (msg.sender.send(shares[msg.sender]))
      shares[msg.sender] = 0;
  }
}
```

Good

```js
contract Fund {
  /// Mapping of ether shares of the contract.
  mapping(address => uint) shares;
  /// Withdraw your share.
  function withdraw() public {
    uint share = shares[msg.sender];
    shares[msg.sender] = 0;
    msg.sender.transfer(share);
  }
}
```

### Gas Limit and Loops

### Sending and Receiving Ether

### Callstack Depth

### tx.origin

### Two's Complement / Underflows / Overflows

### Minor Details

## Recommendations
