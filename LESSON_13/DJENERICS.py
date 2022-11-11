#АННОТАЦИЯ ТИПОВ (ДЖЕЕРИКИ)

def greeting(name: str = "world") -> str:
    return "Hello, " + name

print(greeting())
"""
def body_mass_index(weight: float, height: float) -> float:
    return weight / height ** 2
print(body_mass_index())

def print_hello(name: str, upper: bool = False) -> None:
    if upper:
        name = name.upper()
    print("Hello,", name)
#####################################################################    
name: str = "Andrey"
age: int = 25
is_sick_with_covid19: bool = False  # надеюсь
pi: float = 3.1415

# можно даже аннотировать переменные, не назначая им значения
foo: str
    ##################################################
    from typing import List, Tuple, Dict, Set

# тип всех элементов списка
primes: List[int]

# тип каждого элемента кортежа
person_info: Tuple[str, int, float, float]

# тип ключей, тип значений
stock_prices: Dict[str, float]

# тип всех элементов множества
valid_answers: Set[str]
"""
