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
