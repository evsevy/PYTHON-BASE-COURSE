import keyboard
import time

n = 2
IsAlive = True
def Terminate():
    global IsAlive
    IsAlive = False
keyboard.add_hotkey('esc', Terminate)

while IsAlive:
    n = 2 + (n ** 2) % 2147000000
    print('\r', n, sep='')
    time.sleep(0.2)
