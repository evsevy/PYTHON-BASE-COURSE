"""
##############################################
МИКСИНЫ

Например, возьмите следующие классы

 class Mixin1(object):
    def test(self):
        print "Mixin1"

class Mixin2(object):
    def test(self):
        print "Mixin2"

class BaseClass(object):
    def test(self):
        print "Base"

class MyClass(BaseClass, Mixin1, Mixin2):
    pass

 
В этом случае класс Mixin2 является базовым классом, расширенным с помощью Mixin1 и, наконец, с помощью BaseClass. 
Таким образом, если мы выполним следующий фрагмент кода:

x = MyClass()
x.test()
Base

#1. Используя множественное наследование переопределите метод базового класса
#2. Как можно вызвать переопределнный метод базового класса


class Base():   
    def run(self):
        print ('Base: I can run' )


class Mixin1():
    def run(self):
        print ("Mixin:I can fly")


class SuperMan(Mixin1, Base):
    def doing(self):        
        self.run()       #Замещение базового метода, методом из миксина       
        Base.run(self)   #Вызов Родителя Base с передачей текущего инстанса
        Base.run(Base()) #Вызов Родителя Base с передачей инстанса Base


def main():
    super_man = SuperMan()
    super_man.doing()


if __name__=='__main__':
    main()
    ########################################
    #coding: utf-8
"""
#2.1 Создать класс для работы со списком случайных значений, 
#2.2. Добавить класс миксин helper 
#с методами: показать среднее значение, показать минимальное значение, 
#показать максимальное значение
"""
import random

class SomeBaseList ():
    pass

class Helper():
     миксин helper 
    def __init__(self):
        super().__init__()

    def show_min(self):
        print('Min: {}'.format(min(self._lst)))

    def show_max(self):
        print('Max: {}'.format(max(self._lst)))

    def show_avg(self):
        print('Avg: {}'.format(sum(self._lst) / len(self._lst)))    
        
###############################################
class RandomList(Helper, SomeBaseList):
    # класс для работы со списком случайных значений 
    def __init__(self):
        super().__init__()
        self._lst = []

    def fill(self):
        self._lst = [random.randint(0, 100) for i in range(0,10)]

    def clear(self):
        self._lst = []        

    def show(self):
        print(self._lst)


def main():
    r = RandomList()
    r.fill()
    r.show()
    r.show_min()
    r.show_max()
    r.show_avg()


if __name__=='__main__':
    main()

    ###########################################  

# ПОДКЛЮЧЕНИЕ К IP

import ipaddress


def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as err:
        return False


if __name__ == '__main__':
    ip1 = '10.1.1.1'
    ip2 = '10.1.1'

    print('Проверка IP...')
    print(ip1, check_ip(ip1))
    print(ip2, check_ip(ip2))
################################################################3
#  ИМПОРТ КАРТИНОК

Установка matplotlib:

pip install matplotlib
pip install pillow
#
from matplotlib import pyplot as plt


img = plt.imread('x.jpg')
plt.imshow(img)
plt.show()
################################
from PIL import Image
#...
img = Image.open(r'D:\picture.jpg')
img.show()

# ДЛЯ КОНСОЛИ
import os
os.system("D\picture.jpg")

##################################

import random

class SomeBaseList ():
    pass

class Helper():
    # миксин helper 
    def __init__(self):
        super().__init__()

    def show_min(self):
        print('Min: {}'.format(min(self._lst)))

    def show_max(self):
        print('Max: {}'.format(max(self._lst)))

    def show_avg(self):
        print('Avg: {}'.format(sum(self._lst) / len(self._lst)))    
        

class RandomList(Helper, SomeBaseList):
    # класс для работы со списком случайных значений 
    def __init__(self):
        super().__init__()
        self._lst = []

    def fill(self):
        self._lst = [random.randint(0, 100) for i in range(0,10)]

    def clear(self):
        self._lst = []        

    def show(self):
        print(self._lst)


def main():
    r = RandomList()
    r.fill()
    r.show()
    r.show_min()
    r.show_max()
    r.show_avg()


if __name__=='__main__':
    main()
#####################################################################
СОЗДАНИЕ И ИМПОРТИРОВАНИЕ СОБСТВЕННЫХ МОДУЛЕЙ

Модуль может содержать функции, как уже описано, но также и переменные всех типов (массивы, словари, объекты и т. д.).
Сохраним этот код в файл mymodule.py

person1 = {"name": "Виктор","age": 36,"country": "Россия"}
Импортируем модуль с названием mymodule, и получим доступ к словарю person1:

import mymodulea = mymodule.person1["age"]print(a)
####################################################
Запись объекта Python в файл в формате JSON (файл json_write_dump.py):

import json

trunk_template = [
    'My name is Evgeny merkulov', 'I am a programmer ingener',
    'I was born in Minsk', 'Studied in HAI'
]

access_template = [
    'my working skills are ///', 'my career////',
   
]

to_json = {'trunk': trunk_template, 'access': access_template}

with open('sw_templates.json', 'w') as f:
    json.dump(to_json, f)

with open('sw_templates.json') as f:
    print(f.read())
#################################################
import json

with open('sw_templates.json') as f:
    file_content = f.read()
    templates = json.loads(file_content)

print(templates)

for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))
"""
