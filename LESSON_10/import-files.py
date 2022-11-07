"""
Пишем класс в файле person.py

Нужно описать класс и его конструктор.
Подумаем что нужно хранить о каждом работнике.
Его имя (полное), кем работет, его зарплату.
Человек может еще только приниматься на работу или его уже уволили.
Тогда работы нет и зарплата 0. Запишем это в конструкторе.
"""

class Person(object):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
# Сразу начинаем тестировать класс: создаем экземпляры класса, печатаем значение их полей

class Person(object):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

# Конец класса Person

# Тестируем класс:
evg = Person('EVGEN MERK')
rom = Person('ROMAN MERK', job='student', pay=5000)

print(evg.name, evg.pay)        
print(rom.name, rom.pay)
"""
evg и rom определяют каждое свое пространство имен.
Т.е. поля name и pay в объекте evg не совпадают с полями name и pay в объекте roman,
так как каждый экземпляр класса имеет свой набор атрибутов (name, job, pay).

Тестирование и выполнение
Мы написали тесты, но они всегда выполняются и при import этого модуля. Это не нужно.
Можно тесты положить в отдельные файлы (и это хорошо!).
Можно написать тесты с использованием библиотек docstring, unittest, pytest и так далее.
Пока будем писать тесты в том же файле, но запускать их только тогда, когда мы запускаем непосредственно файл,
а не импортируем его в другие файлы.
python person.py
Для этого будем проверять, как запускается файл, используя атрибут __name__ модуля:
"""
class Person(object):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

# Конец класса Person

if __name__ == '__main__':
    # Тестируем класс, только если запускаем файл
    evg = Person('E V M')
    rom = Person('R V M', job='student', pay=5000)

    print(evg.name, evg.pay)       
    print(rom.name, rom.pay)     
