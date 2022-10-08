# Lesson 3
# FUNCTIONS
# DRY - CONCEPT

""" def my_function(FOR):

    print (FOR + "Hello, World!")
    
my_function("For all people: ")
my_function()
my_function()
my_function() """

# RETURN
""" def greet(name):
    print(f'Hi! {name}')
greet('EVGENY') """

def greet(name):
    return f'Hi! {name}'
print(greet('EVGENY'))

""" Именные функции, инструкция def
Функция в python - объект, принимающий аргументы и возвращающий значение. Обычно функция определяется с помощью инструкции def.

Определим простейшую функцию: """

def add(x, y):
    return x + y
""" Инструкция return говорит, что нужно вернуть значение. В нашем случае функция возвращает сумму x и y.
Теперь мы ее можем вызвать: """
print(add(1, 10))
print(add('abc', 'def'))

""" Функция может быть любой сложности и возвращать любые объекты (списки, кортежи, и даже функции!):

def newfunc(n):
def myfunc(x):
    return x + n
    return myfunc

new = newfunc(100)  # new - это функция
new(200)
300
Функция может и не заканчиваться инструкцией return, при этом функция вернет значение None: """

def func():
    pass
print(func())
None
# Аргументы функции
""" Функция может принимать произвольное количество аргументов или не принимать их вовсе. Также распространены функции с произвольным числом аргументов, функции с позиционными и именованными аргументами, обязательными и необязательными. """

def func(a, b, c=2): # c - необязательный аргумент
    return a + b + c

print(func(1, 2))  # a = 1, b = 2, c = 2 (по умолчанию)
5
func(1, 2, 3)  # a = 1, b = 2, c = 3
6
func(a=1, b=3)  # a = 1, b = 3, c = 2
6
func(a=3, c=6)  # a = 3, c = 6, b не определен
""" Traceback (most recent call last):
  File "", line 1, in
    func(a=3, c=6)
TypeError: func() takes at least 2 arguments (2 given) """
""" Функция также может принимать переменное количество позиционных аргументов, тогда перед именем ставится *: """

def func(*args):
    return args

print(func(1, 2, 3, 'abc'))


""" Как видно из примера, args - это кортеж из всех переданных аргументов функции, и с переменной можно работать также, как и с кортежем. Функция может принимать и произвольное число именованных аргументов, тогда перед именем ставится **: """

def func(**kwargs):
    return kwargs
print(func(a=1, b=2, c=3))

func()
{}
func(a='python')
{'a': 'python'}
""" В переменной kwargs у нас хранится словарь, с которым мы, опять-таки, можем делать все, что нам заблагорассудится. """

""" Анонимные функции, инструкция lambda
Анонимные функции могут содержать лишь одно выражение, но и выполняются они быстрее. Анонимные функции создаются с помощью инструкции lambda. Кроме этого, их не обязательно присваивать переменной, как делали мы инструкцией def func(): """


func = lambda x, y: x + y
print(func(1, 2))

""" lambda функции, в отличие от обычной, не требуется инструкция return, а в остальном, ведет себя точно так же: """

func = lambda *args: args
print(func(1, 2, 3, 4))

# вложенная функция
def function1(): # outer function
    print ("Hello from outer function")
def function2(): # inner function
    print ("Hello from inner function")
function2()

function1()

# вложенная функция может брать переменные из главной
def num1(x):
def num2(y):
    return x * y
    return num2
res = num1(10)

print(res(5))
# ИНКАПСУЛЯЦИЯ  в функции
def outer_function(x):
    # Hidden from the outer code
    def inner_increment(x):
        return x + 2
    y = inner_increment(x)
    print(x, y)

inner_increment(5)
#outer_function(5)

""" ЗАМЫКАНИЕ Цель замыкания состоит в том, чтобы заставить внутреннюю функцию запоминать состояние ее окружения, когда она вызывается, даже если она не находится в памяти. """
def function1(name):
    def function2():
        print('Hello ' + name)
    return function2

func = function1('Nicholas')
func()

""" Вывод: Внутренняя функция-это просто функция, определенная внутри другой функции. Внутренняя функция может получить доступ к переменным, которые были определены в области действия внешней функции, но она не может их изменить. Существует целый ряд причин, по которым нам может понадобиться создать внутреннюю функцию. Например, внутренняя функция защищена от того, что происходит снаружи. Внутренние функции также являются хорошим способом создания замыканий в Python. """
# RECURSION
""" def try_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nРезультаты примера рекурсии")
try_recursion(20) """

# LAMBDA
""" x = lambda a : a / 10
print (x(2147483647)) """

# Свойство анонимности

""" def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# WHILE / FOR
i = 1
while i < 6:
  print(i)
  i += 1
  
  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i уже не меньше, чем 6") """