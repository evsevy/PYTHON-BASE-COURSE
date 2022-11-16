# ПОТОКИ (ПРОДОЛЖЕНИЕ)
"""
import threading
import time

def sum(x, y):
    print(x + y)
    time.sleep(5)

#print(threading.active_count())

print(threading.main_thread())
threading.main_thread().setName('SECOND-NAME')
print(threading.main_thread())
 
#threading.Thread(target=sum, args=(200, 500)).start()
t = threading.Timer(5, sum, args=(200, 500))
t.start()
t.join()
#print('NEW-THREAD')
print(threading.active_count()) # число потоков
print(threading.enumerate()) # выдает потоки
"""

# СЛИЯНИЕ ПОТОКОВ С ПРЕДОСТАВЛЕНИЕМ КАЖДОМУ ВРЕМЕННОГО КОРИДОРА
"""

import threading
import time
import random


def py_sleep(number):
    sleep = random.randrange(1, 8)
    time.sleep(sleep)
    print("THE PYTHON {}, slept for {} seconds".format(number, sleep))


for i in range(9):
    t = threading.Thread(target=py_sleep, args=(i,))
    t.start()

print("All Threads are queued, let's see the finish!")
"""

"""
Итак, особенность Python в том, что он организует потоки вычислений на конкурентной основе.
За это отвечает специальный механизм — глобальный блокировщик интерпретатора (Global Interpreter Lock).
Он следит за тем, чтобы в каждый момент времени в байт-коде Python выполнялся только один поток.
В ранних версиях Python переключение между потоками происходило по достижении заданного
количества операций,сейчас GIL(Global Interpreter Lock) снимает блокировку через определенное количество секунд.
Решение с обходом GIL кроется за модулем мультипроцесса, благодаря которому все же можно задать параллельное исполнение потокам
"""
# запуск функции параллельно в разных (процессах), с помощью использования субпроцессов вместо потоков, точнее для распределения потоков!
from multiprocessing import Pool
import threading

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1, 2, 3, 6, 8]))
    print(threading.enumerate()) # выдает потоки
