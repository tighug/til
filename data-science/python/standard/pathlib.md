# pathlib

```python
from pathlib import Path
```

## Usage

```python
path = Path("./aaa")

path.resolve() # 絶対パス
path.name # ファイル名
path.suffix # 拡張子名
path.exists() # 存在するか

joined_path = path / "bbb" # 連結
```
