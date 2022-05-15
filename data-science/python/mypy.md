# Mypy

## Installation

```bash
poetry add -D mypy
```

## Usage

```bash
mypy [target]
```

## Types

### Variables

```py
from typing import List, Set, Dict, Tuple, Optional

x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"

x: list[int] = [1]
x: set[int] = {6, 7}
x: dict[str, float] = {"field": 2.0}

x: tuple[int, str, float] = (3, "yes", 7.5)
x: tuple[int, ...] = (1, 2, 3)

# Use Optional[] for values that could be None
x: Optional[str] = some_function()
```

### Functions

```py
def plus(num1: int, num2: int) -> int:
    return num1 + num2

x: Callable[[int, float], float] = f

def g(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1
```

### Classes

```py
class MyClass:
    # You can optionally declare instance variables in the class body
    attr: int
    # This is an instance variable with a default value
    charge_percent: int = 100

    # The "__init__" method doesn't return anything, so it gets return
    # type "None" just like any other method that doesn't return anything
    def __init__(self) -> None:
        ...

    # For instance methods, omit type for "self"
    def my_method(self, num: int, str1: str) -> str:
        return num * str1
```

## References

- [mypy](https://mypy.readthedocs.io/en/latest/)
