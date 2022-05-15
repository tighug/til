# TTF

[TTF](https://interwork.org/)（Token Taxonomy Framework）は、トークンを分類して整理したフレームワークのこと。[EEA](https://entethalliance.org/)（Enterprise Ethereum Alliance）を中心に策定が行われている。

## EEA

EEA は、エンタープライズ向け Ethereum の標準化を目指す非営利団体で、2017 年に設立される。OSS のパーミッション型ブロックチェーンである [Quorum](https://www.goquorum.com/) の開発も行っている。

accenture、J.P.Morgan、Intel、Microsoft、ConsenSys などの 200 以上の企業・団体がメンバーとして参加している。

## EEA Trusted Token

トークンのシーケンス図

- [Token Sequence Diagrams](https://github.com/EntEthAlliance/EEA-Trusted-Reward-Token/blob/develop/ttf/grant-flow.md)

TTF によるトークンの仕様

- [TTF EEA Reward Specification](https://github.com/EntEthAlliance/EEA-Trusted-Reward-Token/blob/develop/ttf/EEA-Reward/latest/EEA-Reward-spec.pdf)
- [TTF EEA Reputation Specification](https://github.com/EntEthAlliance/EEA-Trusted-Reward-Token/blob/develop/ttf/EEA-Reputation/latest/EEA-Reputation-spec.pdf)
- [TTF EEA Penalty Specification](https://github.com/EntEthAlliance/EEA-Trusted-Reward-Token/blob/develop/ttf/EEA-Penalty/latest/EEA-Penalty-spec.pdf)

これらのトークンは、 EEA SIGs や TWGs などの**ワーキンググループへの EEA メンバーの組織とその従業員の参加を奨励するため**に利用される。具体的には、これらのトークンを利用して**助成金分配システム**を構築する。

### Business

1. 各組織は、ワーキンググループに対してコミットメント（約束）をする
2. 各組織は、コミットメントを履行できれば**Reward Token**、不履行ならば**Penalty Token**をワーキンググループイベント終了後に Mint される
3. 組織内の各従業員は、貢献度に応じて各トークンが分配される
4. 受け取った **Reward/Penalty Token** の分だけ、各従業員の **Reputation Token**が Mint/Burn される
5. 各組織の **Reputaion Token** は、所属する従業員の所有量の合計になる

### Tokens

#### EEA Reward Token

- 正の報酬（0 以上）を表す
- 譲渡可能
- 金品と交換可能
  - プールされた swag の購入
  - スポンサーの bouncy の購入

#### EEA Penalty Token

- 負の報酬（0 以下）を表す
- 譲渡不可能
- 弁済可能
  - 弁済後は Burn される（報酬の総量は減少）
- Reward Token を利用するには、すべての Penalty Token を弁済しなければならない

#### EEA Reputaion Token

- 0 以上
- Lifetime スコア（生涯継続）
- 譲渡不可
- 金品との交換・弁済不可

### Sharing

**Reward Token**のみ、組織間で交換可能。Reputaion Token が少ないと、所有する Reward Token の価値が低下する。

### Questions

- 誰が助成金システムを制御するのか
  - EEA SIG/TWG の議長
- 誰が助成金を Mint するのか
  - EEA SIG/TWG の議長
- 誰が助成金を寄与するのか
  - EEA のメンバー

### Roles

- EEA Secretary: トークンを配布する
- EEA Organizations
- EEA Members

## References

- [EntEthAlliance/EEA-Trusted-Reward-Token | GitHub](https://github.com/EntEthAlliance/EEA-Trusted-Reward-Token/tree/develop)
