from tkinter import *
import keyboard
import pyautogui

isRun = [False]


def callback():
    if isRun[0]:
        isRun[0] = False
        print("off")
    else:
        isRun[0] = True
        print("on")
    tick()


def tick():
    if not isRun[0]:
        return
    pyautogui.click(button='left')
    root.after(1000, tick)


root = Tk()
keyboard.add_hotkey("f8", callback)
b = Button(root, text="OK", command=callback)
b.pack()

tick()

root.mainloop()
