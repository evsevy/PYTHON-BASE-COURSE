"""
import keyboard

while True:
    keyboard.wait("1")
    keyboard.write("\n The key '1' was pressed!")

import keyboard

keyboard.add_hotkey("ctrl+alt+j", lambda: print("ctrl+alt+j was pressed"))
"""
import keyboard
def fib():
    a, b = 0, 1
    print('Start: s')
    keyboard.wait('s')
    while True:
        yield a
        a, b = b, a + b
    
for i in fib():
    print(i)
    
    if keyboard.is_pressed('p'): #Остановить цикл
       keyboard.wait('p')
    elif keyboard.is_pressed('c'):
        continue
    
#    if i >= 900000000000000000000000000000000000000000000000000000:
#       break

