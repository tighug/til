# Python

## Syntax

### If

```py
if x < 0:
  x = 0
  print('Negative changed to zero')
elif x == 0:
  print('Zero')
elif x == 1:
  print('Single')
else:
  print('More')
```

### For

```py
for w in words:
  print(w, len(w))
```

- `range()`

```py
for i in range(5):
  print(i)
```

```py
range(5, 10) # 5, 6, 7, 8, 9
range(0, 10, 3) # 0, 3, 6, 9
range(-10, -100, -30) # -10, -40, -70

sum(range(4))  # 0 + 1 + 2 + 3
list(range(4)) # [0, 1, 2, 3]
```

- `break`, `continue`

```py
for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      break
  else:
    # loop fell through without finding a factor
    print(n, 'is a prime number')
```

```py
for num in range(2, 10):
  if num % 2 == 0:
    print("Found an even number", num)
    continue
  print("Found an odd number", num)
```

### Pass

何もしない。クラスなどの中身を仮置したい時に使用する。

```py
class MyEmptyClass:
  pass
```

### Function

```py
# write Fibonacci series up to n
def fib(n):
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a+b
  print()
```

- 引数のデフォルト値

```py
def ask_ok(prompt, retries=4, reminder='Please try again!'):
  while True:
    ok = input(prompt)
    if ok in ('y', 'ye', 'yes'):
      return True
    if ok in ('n', 'no', 'nop', 'nope'):
      return False
    retries = retries - 1
    if retries < 0:
      raise ValueError('invalid user response')
    print(reminder)
```

- キーワード引数

```py
parrot(voltage=1000000, action='VOOOOOM')
```

### List

```py
list.append(x) # 末尾に要素を追加
list.extend(iterable) # 末尾にリストを追加
list.insert(i, x) # インデックスiに要素xを追加
list.remove(x) # xと等しい値を持つ最初の要素を削除
list.pop() # 末尾の要素を削除し、その要素を返す
list.pop(i) # インデックスiの要素を削除し、その要素を返す
list.clear() # すべての要素を削除
list.index(x) # xと等しい値を持つ最初の要素のインデックスを返す
list.count(x) # 要素xの個数を返す
list.sort() # ソートする
list.reverse() # 逆順にする
list.copy() # shallowコピーを返す
```

- `del`

```py
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0] # Remove -1
```

- `enumerate()`

```py
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

for i in reversed(range(1, 10, 2)):
    print(i)
```

- `sorted()`

元の配列を変更せず、ソート済みの新たな配列を返す。

```py
sorted(basket)
```

- `set()`

重複要素を除去する。

```py
set(basket)
```

### Tuple

### Dictionary

```py
tel = {'jack': 4098, 'sape': 4139}
tel['jack']
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)
```

- `items()`

```py
for k, v in knights.items():
  print(k, v)
```

### Module

```py
from fibo import fib, fib2
```

### Package

### Exception

```py
try:
    x = int(input("Please enter a number: "))
    break
except ValueError:
    print("Oops!  That was no valid number.  Try again...")
finally:
    print('Goodbye, world!')
```

```py
raise NameError('HiThere')
```

### Class

### Files

## Best Practices

- [The Hitchhiiker's Guide to Python](https://docs.python-guide.org/writing/style/)
- [The Best of the Best Practices (BOBP) Guide for Python](https://gist.github.com/sloria/7001839)

## References

- [Python ドキュメント](https://docs.python.org/ja/3/)
- [The Hitchhiiker's Guide to Python 「プロジェクトの構造化」](https://python-guideja.readthedocs.io/ja/latest/writing/structure.html)
- [ゼロから学ぶ Python](https://rinatz.github.io/python-book/)
