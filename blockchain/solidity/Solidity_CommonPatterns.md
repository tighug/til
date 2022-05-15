# Solidity Common Patterns

- [Common Patterns](https://solidity-jp.readthedocs.io/ja/latest/common-patterns.html)
- [solidity-patterns](https://fravoll.github.io/solidity-patterns/)

## Behavioral

### Guard Check

スマートコントラクトとその入力パラメーターの動作が期待どおりであることを確認する

- `require()`
  - 入力のチェック
  - contract の状態を実行前に戻す
  - 残りのガスを caller に返却
  - 主に関数の最初に行う
- `assert()`
  - 重大なエラーのチェック
  - contract の状態を実行前に戻す
  - 残りのガスを全て消費
  - 主に関数の最後に行う
- `revert()`：
  - ほぼ`require()`の代替
  - 自身で bool 値のチェックを行わない（つまり if 文等で行う）

```js
// This code has not been professionally audited, therefore I cannot make any promises about
// safety or correctness. Use at own risk.
contract GuardCheck {

    function donate(address addr) payable public {
        require(addr != address(0));
        require(msg.value != 0);
        uint balanceBeforeTransfer = this.balance;
        uint transferAmount;

        if (addr.balance == 0) {
            transferAmount = msg.value;
        } else if (addr.balance < msg.sender.balance) {
            transferAmount = msg.value / 2;
        } else {
            revert();
        }

        addr.transfer(transferAmount);
        assert(this.balance == balanceBeforeTransfer - transferAmount);
    }
}
```

### State Machine

状態によって実行可能な関数が移行する。

```js
pragma solidity >=0.4.22 <0.7.0;

contract StateMachine {
    enum Stages {
        AcceptingBlindedBids,
        RevealBids,
        AnotherStage,
        AreWeDoneYet,
        Finished
    }

    // This is the current stage.
    Stages public stage = Stages.AcceptingBlindedBids;

    uint public creationTime = now;

    modifier atStage(Stages _stage) {
        require(
            stage == _stage,
            "Function cannot be called at this time."
        );
        _;
    }

    function nextStage() internal {
        stage = Stages(uint(stage) + 1);
    }

    // Perform timed transitions. Be sure to mention
    // this modifier first, otherwise the guards
    // will not take the new stage into account.
    modifier timedTransitions() {
        if (stage == Stages.AcceptingBlindedBids &&
                    now >= creationTime + 10 days)
            nextStage();
        if (stage == Stages.RevealBids &&
                now >= creationTime + 12 days)
            nextStage();
        // The other stages transition by transaction
        _;
    }

    // Order of the modifiers matters here!
    function bid()
        public
        payable
        timedTransitions
        atStage(Stages.AcceptingBlindedBids)
    {
        // We will not implement that here
    }

    function reveal()
        public
        timedTransitions
        atStage(Stages.RevealBids)
    {
    }

    // This modifier goes to the next stage
    // after the function is done.
    modifier transitionNext()
    {
        _;
        nextStage();
    }

    function g()
        public
        timedTransitions
        atStage(Stages.AnotherStage)
        transitionNext
    {
    }

    function h()
        public
        timedTransitions
        atStage(Stages.AreWeDoneYet)
        transitionNext
    {
    }

    function i()
        public
        timedTransitions
        atStage(Stages.Finished)
    {
    }
}
```

### Oracle

ブロックチェーンの外部に保存されているデータにアクセスする

- Oraclize（Provable）利用例：[flightDelay](https://github.com/etherisc/flightDelay/blob/master/contracts/FlightDelayPayout.sol)
- 投票メカニズム利用例：[Ethersquares](https://github.com/ethersquares/ethersquares-contracts/blob/master/contracts/OwnedScoreOracle.sol)

### Randomness

- ブロックハッシュ PRNG-ランダム性のソースとしてのブロックのハッシュ
- Oracle RNG - Oracle が提供するランダム性、Oracle パターンを参照

## Security

### Access Restriction

実行するアカウントや時間を修飾子で制限する

```js
modifier onlyBy(address _account){
    require(
        msg.sender == _account,
        "Sender not authorized."
    );
    _;
}

modifier onlyAfter(uint _time) {
    require(
        now >= _time,
        "Function called too early."
    );
    _;
}

function disown()
    public
    onlyBy(owner)
    onlyAfter(creationTime + 6 weeks)
{
    delete owner;
}
```

### Checks Effects Interactions

Re-Entrancy（再入攻撃）を回避するために、**① 残高をチェックし**、**② 状態変数を書き換えた後に**、**③Ether の送金を行う**

```js
function withdraw(uint amount) public {
    require(balances[msg.sender] >= amount);

    balances[msg.sender] -= amount;

    msg.sender.transfer(amount);
}
```

### Secure Ether Transfer

基本は`transfer`を使う

| Function     | Amount of Gas Forwarded        | Exception Propagation |
| ------------ | ------------------------------ | --------------------- |
| `send`       | 2300 (not adjustable)          | `false`               |
| `call.value` | all remaining gas (adjustable) | `false`               |
| `transfer`   | 2300 (not adustable)           | throws                |

### Pull over Push

`withdraw()`関数を実装する

### Emergency Stop

緊急時にコントラクトを停止する機能を実装する

## Upgradeability

### Proxy Delegate

### External Storage

## Economic

### String Equality Comparison

### Tight Variable Packing

### Memory Array Building
