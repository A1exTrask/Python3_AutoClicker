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
    Options1 = tk.Tk()
    Options1.title("Clicking options")
    Options1.geometry("274x183")
    Options_But1 = tk.Button(Options1, text='Ok', font="Times 10", padx="17", pady="3")
    Options_But1.place(x=56, y=134)
    Options_But2 = tk.Button(Options1, text='Cancel', font="Times 10", padx="7", pady="3")
    Options_But2.place(x=148, y=134)


def Repeat():
    Repeat1 = tk.Tk()
    Repeat1.title("Clicking repeat")
    Repeat1.geometry("274x183")
    Repeat_But1 = tk.Button(Repeat1, text='Ok', font="Times 10", padx="17", pady="3")
    Repeat_But1.place(x=56, y=134)
    Repeat_But2 = tk.Button(Repeat1, text='Cancel', font="Times 10", padx="7", pady="3")
    Repeat_But2.place(x=148, y=134)


def Multiple_clicks():
    Multiple_clicks1 = tk.Tk()
    Multiple_clicks1.title("Record multiple clicks")
    Multiple_clicks1.geometry("274x183")
    Multiple_clicks_But1 = tk.Button(Multiple_clicks1, text='Ok', font="Times 10", padx="17", pady="3")
    Multiple_clicks_But1.place(x=56, y=134)
    Multiple_clicks_But2 = tk.Button(Multiple_clicks1, text='Cancel', font="Times 10", padx="7", pady="3")
    Multiple_clicks_But2.place(x=148, y=134)


def Hotkey():
    Hotkey1 = tk.Tk()
    Hotkey1.title("Hotkey Setting")
    Hotkey1.geometry("274x183")
    Hotkey_But1 = tk.Button(Hotkey1, text='Ok', font="Times 10", padx="17", pady="3")
    Hotkey_But1.place(x=56, y=134)
    Hotkey_But2 = tk.Button(Hotkey1, text='Cancel', font="Times 10", padx="7", pady="3")
    Hotkey_But2.place(x=148, y=134)


def View():
    View1 = tk.Tk()
    View1.title("View Setting")
    View1.geometry("274x183")
    View_But1 = tk.Button(View1, text='Ok', font="Times 10", padx="17", pady="3")
    View_But1.place(x=56, y=134)
    View_But2 = tk.Button(View1, text='Cancel', font="Times 10", padx="7", pady="3")
    View_But2.place(x=148, y=134)


def Other():
    Other1 = tk.Tk()
    Other1.title("Other Setting")
    Other1.geometry("274x183")
    Other_But1 = tk.Button(Other1, text='Ok', font="Times 10", padx="17", pady="3")
    Other_But1.place(x=56, y=134)
    Other_But2 = tk.Button(Other1, text='Cancel', font="Times 10", padx="7", pady="3")
    Other_But2.place(x=148, y=134)


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
