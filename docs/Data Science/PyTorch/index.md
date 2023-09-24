# PyTorch

PyTorch は、Python のオープンソースの機械学習ライブラリです。

## インストール

```bash
poetry add torch
```

## 使い方

```py
import torch
```

### Tensors

テンソルは配列や行列に似た、特殊なデータ構造です。

標準の配列だけでなく、Numpy 配列からもテンソルに変換できます。

```py
data = [[1, 2],[3, 4]]
tensor = torch.tensor(data) # array to tensor

np_array = np.array(data)
tensor = torch.from_numpy(np_array) # np-array to tensor

np_array = tensor.numpy() # tensor to np-array
```

別のテンソルから新しい特殊なテンソルを作成できます。もとのデータの次元（形）は維持されます。

```py
ones = torch.ones_like(tensor)
# => [[1, 1], [1, 1]]

rand = torch.rand_like(tensor, dtype=torch.float)
# => [[0.1174, 0.0543], [0.0429, 0.3483]]
```

次元からテンソルを作成できます。

```py
shape = (2,3,)
rands = torch.rand(shape)
# => [[0.9763, 0.7324, 0.2759], [0.5884, 0.6512, 0.2697]]

ones = torch.ones(shape)
# => [[1., 1., 1.], [1., 1., 1.]]

zeros = torch.zeros(shape)
# => [[0., 0., 0.], [0., 0., 0.]]
```

テンソルは結合できます。

```py
t1 = torch.cat([tensor, tensor, tensor], dim=1)
```

算術演算が可能です。

```py
# 内積
y1 = tensor @ tensor.T
y2 = tensor.matmul(tensor.T)
y3 = torch.rand_like(y1)
torch.matmul(tensor, tensor.T, out=y3)

# 外積
z1 = tensor * tensor
z2 = tensor.mul(tensor)
z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)
```

単一の要素は数値に変換できます。

```py
agg = tensor.sum()
agg_item = agg.item()
```

### Datasets

あらかじめ用意されたデータセットを読み込めます。

```py
from torchvision import datasets
from torchvision.tranforms import ToTensor

training_data = datasets.FashionMNIST(
    root="data",    # データディレクトリのパス
    train=True,     # 訓練データか、テストデータか
    download=True,  # データが存在しない場合、ダウンロードする
    transform=ToTensor() # 特徴量の変換方法
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)
```

カスタムデータセットクラスを自作できます。このとき、以下 3 つの関数を実装する必要があります。

-   `__init__` : コンストラクタ。
-   `__len__` : データセットのサンプル数を返します。
-   `__getitem__` : 指定されたインデックスに該当するサンプルを返します。

```py
import os
import pandas as pd
from torchvision.io import read_image

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
```

### DataLoaders

データローダーを利用すると、ミニバッチ処理を簡単に行えます。

```py
from torch.utils.data import DataLoader

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)
```

### Transforms

データセットを読み込む際に、ラベルと特徴量の変換方法をそれぞれ指定できます。

```py
import torch
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

ds = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
)
```

### ニューラルネットワークの構築

ニューラルネットワークは、データに対して演算を行うモジュール（層）から構成されます。PyTorch のすべてのモジュールは`nn.Module`のサブクラスです。すべてのモジュールは入力データの演算を行う`forward`メソッドを実装する必要があります。

```py
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
```

以下のモジュールはあらかじめ用意されています。

```py
from torch import nn

flatten = nn.Flatten()
linear = nn.Linear()
relu = nn.ReLU()
seq = nn.Sequentila()
softmax = nn.Softmax()
```

### 自動微分

ニューラルネットワークの学習では、誤差逆伝播法（Back Propagation）というアルゴリズムをよく用います。誤差逆伝播法では、与えられたパラメータに対する損失関数の勾配に従い、モデルの重みを調整します。

この勾配を計算するために、PyTorch では`torch.autograd`という微分エンジンが備わっています。

```py
import torch

x = torch.ones(5)  # input tensor
y = torch.zeros(3)  # expected output
w = torch.randn(5, 3, requires_grad=True)
b = torch.randn(3, requires_grad=True)
z = torch.matmul(x, w)+b
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)

loss.backward()
print(w.grad)
print(b.grad)
```

forward 計算をしたいだけの場合は、トラッキングを無効にできます。たとえば、以下のような場合にはトラッキングを無効にします。

-   事前学習されたネットワークを微調整するときなど、パラメータを固定したい場合。
-   計算を高速化したい場合。

```py
z = torch.matmul(x, w)+b
print(z.requires_grad)

with torch.no_grad():
    z = torch.matmul(x, w)+b
print(z.requires_grad)
```

### モデルパラメータの最適化

データとモデルを準備できたら、モデルを訓練・検証・テストを繰り返し行うことで最適化します。

最適化のために、まずハイパーパラメーターを設定します。ハイパーパラメーターは、最適化処理を制御するためのパラメーターです。この値により、モデルの学習率や収束率が変化します。

-   エポック数 : データセットを繰り返し処理する回数
-   バッチサイズ : データサンプルの数
-   学習速度 : 各バッチ・エポックごとにモデルパラメータをどの程度変化させるか。
    -   値が小さい : 学習速度は遅いが収束しやすい
    -   値が大きい : 学習速度は早いが発散しやすい

### モデルのセーブ&ロード

`torch.save()`と`torch.load()`メソッドを使うと、それぞれモデルの保存と読み込みが可能です。`model.state_dict()`を使わずに、直接`model`を保存することも可能ですが、保存ファイル容量が増加するため推奨されません。

```py
import torch
import torchvision.models as models

# Save
model = models.vgg16(pretrained=True)
torch.save(model.state_dict(), 'model_weights.pth')

# Load
model = models.vgg16() # we do not specify pretrained=True, i.e. do not load default weights
model.load_state_dict(torch.load('model_weights.pth'))
model.eval()
```

## 参考文献

-   [PyTorch](https://pytorch.org/)
