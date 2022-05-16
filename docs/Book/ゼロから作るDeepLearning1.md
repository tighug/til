# ゼロから作る Deep Learning 1

## 2. パーセプトロン

- 複数の信号を入力すると、ひとつの信号を出力するアルゴリズム
- 出力は 0/1

$$
y=
\begin{cases}
0 & (b+\omega_1x_1+\omega_2x_2 \leq 0) \\
1 &(b+\omega_1x_1+\omega_2x_2 > 0)
\end{cases}
$$

- 論理回路を表現できる
  - AND・OR・NAND は一層で表現できる（線形）
  - XOR は二層で表現できる（非線形）

## 3. ニューラルネットワーク

- 中間層の活性化関数
  - シグモイド関数
  - ステップ関数
  - ReLU 関数
- 出力層の活性化関数
  - 恒等関数（回帰問題）
  - ソフトマックス関数（分類問題）

## 4. ニューラルネットワークの学習

- 損失関数（loss function）
  - 二乗和誤差（sum of squared error）
  - 交差エントロピー誤差（cross entropy error）

## 5. 誤差逆伝播法

## 6. 学習に関するテクニック

### 最適化

- SGD
- Momentum
- AdaGrad
- Adam

### 重みの初期値

- ReLU → He の初期値
- sigmoid、tanh → Xavier の初期値

### Batch Normalization

### 過学習

- Weight decay
- Dropout

### ハイパーパラメータの検証

## 7. 畳み込みニューラルネットワーク

## 8. ディープラーニング
