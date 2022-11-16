#KEYBOARD MODUL


i = input('Клавиша: ')
if i == 'a':
    print('ZOPA')
else:
    print( "END!")

f=True
while f:
    #программа
    f = True if input('Начать заново?(Y/N)') == 'Y' else False


"""

# https://github.com/boppreh/keyboard

keyboard.write(message, [delay])- пишет сообщение с задержкой или без нее.

keyboard.wait(key) - блокирует программу до тех пор, пока не будет нажата клавиша. Ключ передается в виде строки ("пробел", "esc" и т.д.)


pip install keyboard

keyboard.press(key)- нажимает клавишу и удерживается до вызова функции release(key)

keyboard.release(key)- выпускает ключ.

keyboard.send(key)- нажимает и отпускает клавишу.

keyboard.add_hotkey(hotkey, function)- создает hotkey,
которая при нажатии выполняет function.

keyboard.record(key)- записывает активность клавиатуры до нажатия key.

keyboard.play(recorded_events, [speed_factor]) - воспроизводит события,
записанные with keyboard.record(key) функция,
с дополнительным speed_factor.

import keyboard


def foo():
    print('World')


keyboard.add_hotkey('Ctrl + 1', lambda: print('Hello'))
keyboard.add_hotkey('Ctrl + 2', foo)

keyboard.wait('Ctrl + Q')

#############################################
import keyboard

while True:
    keyboard.wait("1")
    keyboard.write("\n The key '1' was pressed!")

#################################################
import keyboard

recorded_events = keyboard.record("s")

keyboard.send("w")
keyboard.send("a")

keyboard.play(recorded_events)
###########################################


# pip install pynput
from pynput.keyboard import Key, Listener


def on_press(key):
    print('{0} pressed'.format(key))


def on_release(key):
    print('{0} release'.format(key))

    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

import keyboard
keyboard.add_abbreviation("@", "john@stackabuse.com")

import keyboard

keyboard.add_hotkey("ctrl+alt+j", lambda: print("ctrl+alt+j was pressed"))

import keyboard

while True:
  print('waiting...')
  key = keyboard.read_key()
  print(key)
  if key in ['5', '6']:
    print('OK')
    break
"""    
