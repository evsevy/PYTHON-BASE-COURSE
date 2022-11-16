import threading
import time
def myfunc(a, b):
    time.sleep(6.5)
    print('сумма :', a + b)
thr1 = threading.Thread(target = myfunc, args = (1, 2), daemon=True)
thr1.start()
thr1.join(1.5)
if thr1.is_alive():
    print('поток не успел завершиться')
else:
    print('вычисления завершены')


    import threading 
stop = False
def myfunc():
    global stop
    while stop == False:
        pass
thr1 = threading.Thread(target = myfunc) 
thr1.start() 
stop = True
while thr1.is_alive() == True: 
    pass
print('поток завершился')

