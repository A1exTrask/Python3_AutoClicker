from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser
from tkinter.ttk import Combobox
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


def disable_x():
    pass


def Options():
    Options1 = Toplevel()
    Options1.title("Clicking options")
    Options1.geometry("274x183")
    Options1.resizable(False, False)
    Options1.protocol("WM_DELETE_WINDOW", disable_x)
    Label(Options1, text='Mouse:', font='Times 10').place(x=11, y=14)
    Combobox(Options1, values=('Left', 'Right', 'Middle')).place(x=63, y=14)
    Label(Options1, text='Click:', font='Times 10').place(x=11, y=53)
    Combobox(Options1, values=('Single', 'Double')).place(x=63, y=53)
    Checkbutton(Options1, text="Freeze the pointer (only single clik)", onvalue=1, offvalue=0).place(x=10, y=92)
    tk.Button(Options1, text='Ok', font="Times 10", padx="17", pady="3").place(x=56, y=134)
    tk.Button(Options1, text='Cancel', font="Times 10", padx="7", pady="3", command=Options1.destroy).place(x=148, y=134)


def Repeat():
    Repeat1 = Toplevel()
    Repeat1.title("Clicking repeat")
    Repeat1.geometry("400x190")
    Repeat1.resizable(False, False)
    Repeat1.protocol("WM_DELETE_WINDOW", disable_x)
    Label(Repeat1, text='interval:', font='Times 10').place(x=11, y=107)
    Label(Repeat1, text='hours', font='Times 10').place(x=200, y=110)
    Label(Repeat1, text='mins', font='Times 10').place(x=250, y=110)
    Label(Repeat1, text='secs', font='Times 10').place(x=300, y=110)
    Label(Repeat1, text='milliseconds', font='Times 10').place(x=333, y=110)
    tk.Button(Repeat1, text='Ok', font="Times 10", padx="17", pady="3").place(x=121, y=147)
    tk.Button(Repeat1, text='Cancel', font="Times 10", padx="7", pady="3", command=Repeat1.destroy).place(x=210, y=147)


def Multiple_clicks():
    Multiple_clicks1 = Toplevel()
    Multiple_clicks1.title("Record multiple clicks")
    Multiple_clicks1.geometry("274x183")
    Multiple_clicks1.resizable(False, False)
    Multiple_clicks1.protocol("WM_DELETE_WINDOW", disable_x)
    tk.Button(Multiple_clicks1, text='Ok', font="Times 10", padx="17", pady="3").place(x=56, y=134)
    tk.Button(Multiple_clicks1, text='Cancel', font="Times 10", padx="7", pady="3", command=Multiple_clicks1.destroy).place(x=148, y=134)


def Hotkey():
    Hotkey1 = Toplevel()
    Hotkey1.title("Hotkey Setting")
    Hotkey1.geometry("274x183")
    Hotkey1.resizable(False, False)
    Hotkey1.protocol("WM_DELETE_WINDOW", disable_x)
    tk.Button(Hotkey1, text='Ok', font="Times 10", padx="17", pady="3").place(x=56, y=134)
    tk.Button(Hotkey1, text='Cancel', font="Times 10", padx="7", pady="3", command=Hotkey1.destroy).place(x=148, y=134)


def View():
    View1 = Toplevel()
    View1.title("View Setting")
    View1.geometry("274x183")
    View1.resizable(False, False)
    View1.protocol("WM_DELETE_WINDOW", disable_x)
    python_lang = IntVar()
    python_checkbutton = Checkbutton(View1, text="Python", variable=python_lang,
                                     onvalue=1, offvalue=0, padx=15, pady=10)
    python_checkbutton.grid(row=0, column=0, sticky=W)
    javascript_lang = IntVar()
    javascript_checkbutton = Checkbutton(View1, text="JavaScript", variable=javascript_lang,
                                         onvalue=1, offvalue=0, padx=15, pady=10)
    javascript_checkbutton.grid(row=1, column=0, sticky=W)
    tk.Button(View1, text='Ok', font="Times 10", padx="17", pady="3").place(x=56, y=134)
    tk.Button(View1, text='Cancel', font="Times 10", padx="7", pady="3", command=View1.destroy).place(x=148, y=134)


def Other():
    Other1 = Toplevel()
    Other1.title("Other Setting")
    Other1.geometry("274x183")
    Other1.resizable(False, False)
    Other1.protocol("WM_DELETE_WINDOW", close_event_disable)
    tk.Button(Other1, text='Ok', font="Times 10", padx="17", pady="3").place(x=56, y=134)
    tk.Button(Other1, text='Cancel', font="Times 10", padx="7", pady="3", command=Other1.destroy).place(x=148, y=134)


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
root.resizable(False, False)
root.attributes('-topmost', 1)

main_menu = tk.Menu()

file_menu = tk.Menu(tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)

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

tk.Button(root, text='Press F8 to click', padx="53", pady="5", cursor="hand2", command=click).place(x=15, y=12)
tk.Button(root, text="Help >>", padx="72", pady="5", cursor="hand2", command=callback).place(x=15, y=60)

root.mainloop()
