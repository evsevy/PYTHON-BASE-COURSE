import keyboard

def foo():
    print('World')

keyboard.add_hotkey('Ctrl + 1', lambda: print('Hello'))
keyboard.add_hotkey('Ctrl + 2', foo)

keyboard.wait('Ctrl + Q')
