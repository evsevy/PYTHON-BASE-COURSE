"""
# АННОТАЦИЯ ТИПОВ

from typing import Union


d = Union[int, float]
# int | float альтернативная запись python 3.10

def func(x: d, y: int  ) -> float:
    return x * y

result = func(12.4, 34)
print(result)
print(func.__annotations__)

"""
#МОДУЛЬ PANDAS
import pandas as pd
import numpy as np

df = pd.DataFrame({'DATE': [1, 2, 3, 4, 5],
                   'VOLUME': [100, 200, 300,400,500],
                   'PRICE': [214, 234, 253,272,291]})


#
df.shift(1)
print(df)



# eval(input("Введите математическое выражение: "))

# создание списка из чисел
"""
entered_list = input("Введите список чисел, разделенных пробелом: ").split()
print("Введенный список:", entered_list)

num_list = list(map(int, entered_list))
print("Список чисел: ", num_list)
print("Сумма списка:", sum(num_list))
"""


# вставка функции в список данных:
"""
def square(n): return n**2

def cube(n): return n**3

operations = [square, cube]
numbers = [2, 1, 3, 4, 7, 11, 18, 29]
for i, n in enumerate(numbers):
    action = operations[i % 2]
    print(f"{action.__name__}({n}):", action(n))
"""

"""

def square(n): return n ** 2


operations = [square]
numbers = input("Введите список чисел, разделенных пробелом: ").split()
num_list = list(map(int, numbers))

for i, n in enumerate(numbers):
    action = operations[i % 1]
    print(f"{action.__name__}({n}):", action(n))

"""

"""
Допустим, вы потратили 28 литров на 300 километров пути.
Вычисления будут такими: 28 / 300 x 100 = 9,3 л/100 км.
"""
"""
def result(num_my):
    num = [54,24,34,1,2,3]
    return [number for number in num if number in num_my]

"""
from functools import singledispatch


@singledispatch
def main(args):
    raise TypeError("Unacceptable data type")


@main.register(dict)
def _(args):
    print("That\'s dict!", args)


@main.register(list)
def _(args):
    print("That\'s list!", args)


main({1: 2})
main([1, 2])

#########################
import threading

class MyThread(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x

    def run(self):
        print('Starting processing %i...' % x)
        is_prime(self.x)
###############

a = input('INPUT PLEASE:').split()
b = input('INPUT ELSE:').split()
c = [a[i]+b[i] for i in range(min(len(a), len(b)))]
print(c)
#встроенные функции классы и обьекты
"""
for e in __builtins__.__dict__:
    print(e)

"""








