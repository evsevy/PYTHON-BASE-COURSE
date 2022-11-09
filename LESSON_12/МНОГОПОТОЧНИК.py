# МНОГОПОТОЧНЫЙ ПРОЦЕСС

#Это очень полезный метод для экономии времени и повышения производительности приложения.
#Многопоточность позволяет программисту разделять задачи приложения на подзадачи и одновременно запускать их в программе.
#Это позволяет потокам обмениваться данными и совместно использовать ресурсы, такие как файлы, данные и память, одному и тому же процессору.
#Кроме того, это увеличивает скорость отклика пользователя, чтобы продолжить выполнение программы, даже если часть приложения имеет длину или заблокирована.
"""
Методы класса потока
Методы Описание start()
Метод start() используется для инициирования активности потока.
И он вызывается только один раз для каждого потока, чтобы можно было начать выполнение потока.
run() Метод run() используется для определения активности потока и может быть переопределен классом, расширяющим класс потоков.
join() Метод join() используется для блокировки выполнения другого кода до завершения потока.
"""
"""
import threading

def print_hello(n):
    print("Hello, how old are you ", n)
t1 = threading.Thread( target = print_hello, args =(18, ))

t1.start()
"""

import threading
def print_hello(n):
    print("Hello, how much are you? ", n)
T1 = threading.Thread( target = print_hello, args =(2000, ))
T1.start()
T1.join()
print("Thank you")


"""


import threading
def proc(n):
    print ("Процесс", n)
p1 = threading.Thread(target=proc, name="t1", args=["1"])
p2 = threading.Thread(target=proc, name="t2", args=["2"])
p1.start()
p2.start()

###########################################

import threading
def proc(n):
    print ("Процесс", n)
p1 = threading.Thread(target=proc, name="t1", kwargs={"n": "1"})
p2 = threading.Thread(target=proc, name="t2", kwargs={"n": "2"})
p1.start()
p2.start()

#########################################

import threading

class T(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self, name="t" + n)
        self.n = n
    def run(self):
        print ("Процесс", self.n)
p1 = T("1")
p2 = T("2")
p1.start()
p2.start()
"""
