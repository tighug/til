# RNN

## 意味のベクトル化

### word2vec

- 単語分散表現（distributed representation word embedding）
  - 単語をベクトルで表すこと
  - 意味が似ている単語は近く、似ていない単語は遠く
- 種類 : 2x3=6 通り
  - モデル : CBOW / skip-gram
  - 学習の高速化 : なし / hierarchical softmax / negative sampling
- CBOW（Continuous Bag-Of-Words）
  - 穴埋め問題
  - 次元圧縮（分散表現）して予測する 2 層 NN
- skip-gram
  - 周辺単語の予測
- hierarchical softmax
  - softmax 計算の高速化
  - 2 分類を約$log_2V$回計算
- negative sampling
  - 正解 1 個、不正解 9999999... 個は大変
  - 正例 1 個、負例 10 個の 2 分類に変更
  - ロジスティック回帰で学習

進化版

- fasttext
  - skip-gram & negative sampling を工夫
  - characte n-gram

### doc2vec

- 感情分析
- 情報抽出
- 2 つのモデルからなる
  - PV-DM（Distributed Memory Model of Phrase Vector）
  - PV-DBOW（Distributed Bag-Of-Words model of Phrase Vector）

## モデル

```math
(y^{(t)}, h^{(t)}) = f(x^{(t)}, y^{(t-1)}, h^{(t-1)}) \\
```

1. seq2vec
2. vec2seq
3. seq2seq

### Simple RNN

```math
y^{(t)} = h^{(t)} = tanh(x^{(t)}W_{xh}+h^{(t-1)}W_{hh}+b_n)
```

### GRU（Gated Recurrent Unit）

```math
\begin{align}
& z^{(t)} = f_z^\sigma(x^{(t)}, h^{(t-1)}) \\
& r^{(t)} = f_r^\sigma(x^{(t)}, h^{(t-1)}) \\
& \tilde{h}^{(t)} = f_h^{tanh}(x^{(t)}, r^{(t)} \circ h^{(t-1)}) \\
& h^{(t)} = (1-z^{(t-1)}) \circ h^{(t-1)} + z^{(t)} \circ \tilde{h}^{(t)}
\end{align}
```

- $z^{(t)}$ : update gate vector
  - どの程度$h^{t}$を更新するか
- $r^{(t)}$ : reset gate vector
  - どの程度$h^{t}$を忘れるか

### LSTM（Long Short Term Memory）

```math
\begin{align}
& f^{(t)} = f_f^\sigma(x^{(t)}, h^{(t-1)}) \\
& i^{(t)} = f_i^\sigma(x^{(t)}, h^{(t-1)}) \\
& o^{(t)} = f_o^\sigma(x^{(t)}, h^{(t-1)}) \\
& \tilde{c}^{(t)} = f_{\tilde{c}}^{tanh}(x^{(t)}, h^{(t-1)}) \\
& c^{(t)} = f^{(t)} \circ c^{(t-1)} + i^{(t)} \circ \tilde{c}^{(t)}
\end{align}
```

- $f^{(t)}$ : forget gate vector
- $i^{(t)}$ : input gate vector
- $o^{(t)}$ : output gate vector
- $c^{(t)}$ : context vector

### bi-LSTM（Bidirectional LSTM）

- forward LSTM
- backward LSTM

### RNNLM（RNN Language Model）

- PPL（perplexity）: 困惑度、迷っている単語の候補数
- WER（Word Error Ratee）: 誤認識率

### Attention

- Transformer の元ネタ
- Encoder-Decoder の限界
  - 間のベクトルが固定次元なので、長文に対応不可能
-
