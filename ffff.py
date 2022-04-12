import keyboard
import mouse
import time

Clicking = False


def click():
    while True:
        global Clicking
        if Clicking:
            Clicking = False
            print("отключен")
        else:
            Clicking = True
            print("включен")


keyboard.add_hotkey("f8", click)

while True:
    if Clicking:
        mouse.double_click(button='left')
        time.sleep(0.1)
