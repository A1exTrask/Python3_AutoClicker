import tkinter as tk
from tkinter import messagebox
import webbrowser
import keyboard
import pyautogui
import time

stopKey = "f8"
maxX, maxY = pyautogui.size()


def click():
    while True:
        if keyboard.is_pressed(stopKey):
            break
        else:
            pyautogui.click(button='left')
            time.sleep(0.1)
            pyautogui.moveTo(maxX / 2, maxY / 2)


def Exit():
    root.destroy()  # Закрытие


def Options():
    Options = tk.Tk()
    Options.title("Clicking options")
    Options.geometry("274x183")


def Repeat():
    Repeat = tk.Tk()
    Repeat.title("Clicking repeat")
    Repeat.geometry("274x183")


def Multiple_clicks():
    Multiple_clicks = tk.Tk()
    Multiple_clicks.title("Record multiple clicks")
    Multiple_clicks.geometry("274x183")


def Hotkey():
    Hotkey = tk.Tk()
    Hotkey.title("Hotkey Setting")
    Hotkey.geometry("274x183")


def View():
    View = tk.Tk()
    View.title("View Setting")
    View.geometry("274x183")


def Other():
    Other = tk.Tk()
    Other.title("Other Setting")
    Other.geometry("274x183")


def callback():
    webbrowser.open_new(r"https://github.com/A1exTrask/Python3_AutoClicker")


def About():
    messagebox.showinfo(title='About', message='Auto Clicker \n \n Version 1.0', icon='info')


root = tk.Tk()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.geometry('230x110')
root.title('Auto Clicker')
root.resizable(width=False, height=False)
root.attributes('-topmost', 1)

main_menu = tk.Menu()

file_menu = tk.Menu(tearoff=0)
file_menu.add_command(label="Exit", command=Exit)

Options_menu = tk.Menu(tearoff=0)

Clicking_menu = tk.Menu(Options_menu, tearoff=0)

Clicking_menu.add_command(label="Options", command=Options)
Clicking_menu.add_command(label="Repeat", command=Repeat)

Recording_menu = tk.Menu(Options_menu, tearoff=0)

Recording_menu.add_command(label="Multiple clicks", command=Multiple_clicks)

Settings_menu = tk.Menu(Options_menu, tearoff=0)

Settings_menu.add_command(label="Hotkey", command=Hotkey)
Settings_menu.add_command(label="View", command=View)
Settings_menu.add_command(label="Other", command=Other)

Options_menu.add_cascade(label="Clicking", menu=Clicking_menu)
Options_menu.add_cascade(label="Recording", menu=Recording_menu)
Options_menu.add_cascade(label="Settings", menu=Settings_menu)

Help_menu = tk.Menu(tearoff=0)
Help_menu.add_command(label="How to automate a sequence of mouse clicks and keystrokes", command=callback)
Help_menu.add_command(label="About", command=About)

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Options", menu=Options_menu)
main_menu.add_cascade(label="Help", menu=Help_menu)

root.config(menu=main_menu)

m1 = tk.Button(root, text='Press F8 to click', padx="53", pady="5", cursor="hand2", command=click)
m1.place(x=15, y=12)
m2 = tk.Button(root, text="Help >>", padx="72", pady="5", cursor="hand2", command=callback)
m2.place(x=15, y=60)

root.mainloop()
