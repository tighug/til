# NumPy

NumPy は化学計算のためのパッケージです。

## Installation

```bash
poetry add numpy
```

インポート

```py
import numpy as np
```

## Usage

### 配列の作成

```py
np.zeros(2)   # array([0,0])
np.ones(2)    # array([1,1])

np.arange(4)        # array([0,1,2,3])
np.arrange(2, 9, 2) # array([2,4,6,8])
```

### 配列の並べ替え

```py
np.sort([2,1,5])  # array([1,2,5])
```

### 配列の連結

```py
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a, b))  # array([1,2,3,4,5,6,7,8])
```

## APIs

## Array | `ndarray`

```py
ndarray.ndim # 配列の次元数
ndarray.shape # 各次元の配列のサイズ、n行m列では(n,m)
ndarray.size # 配列の全要素数、nxm
ndarray.dtype # 配列の要素の型
ndarray.itemsize # 配列の各要素のbyteサイズ
ndarray.data #
```

配列の生成

```py
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3], [4, 5, 6])
c = np.array([[1, 2], [3, 4]], dtype=complex)

d = np.zeros((3, 4))
e = np.ones((2, 3, 4), dtype=np.int16)
f = np.empty((2, 3))
g = np.arange(10, 30, 5)
h = np.linspace(0, 2, 9)
```

## References

- [NumPy Manual](https://numpy.org/doc/stable/)
