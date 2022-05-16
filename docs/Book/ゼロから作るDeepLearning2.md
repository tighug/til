# ゼロから作る Deep Learning 2

## 1. ニューラルネットワークの復習

損失関数

- 交差エントロピー誤差（Cross Entropy Error）
  - Softmax with Loss

学習手順

1. ミニバッチ
2. 勾配の算出
3. パラメータの更新
4. 1〜3 を繰り返す

学習の最適化

- SGD（Stochastic Gradient Descent）
- Momentum
- AdaGrad
- Adam

高速化

- ビット精度（32bit）
- GPU 計算（CuPy）

## 2. 自然言語と単語の分散表現

- シソーラス（thesaurus）: 類語辞書
  - WordNet
- カウントベース
  - コーパス（corpus）: 大量のテキストデータ
    - PTB（Penn Treebank）
  - 分散表現 : 単語の意味をベクトルで表すこと
  - 分布仮説（distributional hypothesis）: 単語の意味は、周囲の単語によって形成される
  - 共起行列（co-occurence matrix）: 共起する単語のテーブル
  - コサイン類似度
  - 相互情報量（PMI : Pointwise Mutual Information）
  - 次元削減（dimentionality reduction）
    - 特異値分解（Singular Value Decomposition : SVD）
- 推論ベース
  - カウントベースでは膨大な計算コストが必要
  - word2vec

## 3. word2vec

- CBOW
- skip-gram

## 4. word2vec の高速化

- Embedding レイヤ
- Negative Sampling

## 5. RNN

## 6. ゲート付き RNN

## 7. RNN による文章生成

## 8. Attention
