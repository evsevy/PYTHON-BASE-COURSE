# АННОТАЦИЯ ТИПОВ

from typing import Union


d = Union[int, float]
# int | float альтернативная запись python 3.10

def func(x: d, y: int  ) -> float:
    return x * y

result = func(12.4, 34)
print(result)
print(func.__annotations__)
