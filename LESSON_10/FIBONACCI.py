
"""
fib1 = fib2 = 1
 
n = input("Номер элемента ряда Фибоначчи: ")
n = int(n) - 2
 
while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1
 
print("Значение этого элемента:", fib2)

fib1 = fib2 = 1
 
n = int(input())
 
print(fib1, fib2, end=' ')
 
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
    
    def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(10))

#лямбда-фибоначчи
fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
print(fib(2))
"""
# две лямбда-функции, вторая в качестве параметра первой:

_list = [[10,6,9],[0, 14, 16, 80],[8, 12, 30, 44]]
sorted_list = lambda x: (sorted(i) for i in x)
second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
result = second_largest(_list, sorted_list)
print(result)
