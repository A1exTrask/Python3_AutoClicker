import tkinter as tk
import webbrowser
from tkinter import messagebox, W
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton
from PIL import Image
from pystray import MenuItem, Menu, Icon

import keyboard
import pyautogui

#  /////////////////////////////////////////////

isRun = [False]
time_interval = 1000


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
    # root.after(3000, lambda: pyautogui.click(button='left'))
    pyautogui.click(button='left')
    root.after(time_interval, tick)


#  /////////////////////////////////////////////


def disable_x():
    pass


def Options():
    Options1 = tk.Toplevel()
    Options1.title("Clicking options")
    Options1.geometry("274x183")
    Options1.grab_set()
    Options1.resizable(False, False)
    Options1.attributes('-topmost', 1)
    Options1.protocol("WM_DELETE_WINDOW", disable_x)
    tk.Label(Options1, text='Mouse:', font='Times 10').place(x=11, y=14)
    Combobox(Options1, values=('Left', 'Right', 'Middle'), state="readonly", width=8).place(x=63, y=14)
    tk.Label(Options1, text='Click:', font='Times 10').place(x=11, y=53)
    Combobox(Options1, values=('Single', 'Double'), state="readonly", width=8).place(x=63, y=53)
    tk.Checkbutton(Options1, text="Freeze the pointer (only single clik)", onvalue=1, offvalue=0).place(x=10, y=92)
    tk.Button(Options1, text='Ok', font="Times 10", padx="17", pady="3").place(x=56, y=134)
    tk.Button(Options1, text='Cancel', font="Times 10", padx="7", pady="3", command=Options1.destroy).place(x=148, y=134)


def Repeat():
    Repeat1 = tk.Toplevel()
    Repeat1.title("Clicking repeat")
    Repeat1.geometry("400x190")
    Repeat1.grab_set()
    Repeat1.resizable(False, False)
    Repeat1.attributes('-topmost', 1)
    Repeat1.protocol("WM_DELETE_WINDOW", disable_x)
    frame = tk.LabelFrame(Repeat1, padx="127", pady="19")
    frame.place(x=5, y=6)
    Radiobutton(frame, text="Repeat", value=1).grid(row=0, column=0, sticky=W)  # переделать находится в центре
    Radiobutton(frame, text="Repeat until stopped", value=2).grid(row=1, column=0, sticky=W)  # переделать находится в центре
    tk.Spinbox(frame, width=7, justify=tk.RIGHT, from_=1, to=16959).place(x=70, y=3)
    tk.Label(frame, text='times', font='Times 10').place(x=130, y=3)
    tk.Label(Repeat1, text='interval:', font='Times 10').place(x=11, y=107)
    tk.Label(Repeat1, text='hours', font='Times 10').place(x=121, y=110)
    tk.Label(Repeat1, text='mins', font='Times 10').place(x=190, y=110)
    tk.Label(Repeat1, text='secs', font='Times 10').place(x=252, y=110)
    tk.Label(Repeat1, text='milliseconds', font='Times 10').place(x=315, y=110)
    tk.Entry(Repeat1, justify=tk.RIGHT, width=4).place(x=93, y=110)
    tk.Entry(Repeat1, justify=tk.RIGHT, width=4).place(x=161, y=110)
    tk.Entry(Repeat1, justify=tk.RIGHT, width=4).place(x=225, y=110)
    tk.Entry(Repeat1, justify=tk.RIGHT, width=4).place(x=287, y=110)
    tk.Button(Repeat1, text='Ok', font="Times 10", padx="17", pady="3").place(x=121, y=147)
    tk.Button(Repeat1, text='Cancel', font="Times 10", padx="7", pady="3", command=Repeat1.destroy).place(x=210, y=147)


def Multiple_clicks():
    Multiple_clicks1 = tk.Toplevel()
    Multiple_clicks1.title("Record multiple clicks")
    Multiple_clicks1.geometry("284x175")
    Multiple_clicks1.grab_set()
    Multiple_clicks1.resizable(False, False)
    Multiple_clicks1.attributes('-topmost', 1)
    Multiple_clicks1.protocol("WM_DELETE_WINDOW", disable_x)
    tk.Checkbutton(Multiple_clicks1, text="Record and replay multiple clicks", onvalue=1, offvalue=0).place(x=10, y=12)
    tk.Label(Multiple_clicks1, text='Click records:').place(x=10, y=45)
    tk.Entry(Multiple_clicks1, justify=tk.RIGHT, width=12).place(x=110, y=45)
    tk.Button(Multiple_clicks1, text='Pick point', padx="12", pady="15").place(x=192, y=50)
    tk.Button(Multiple_clicks1, text='Clear', padx="20", pady="1").place(x=110, y=78)
    tk.Button(Multiple_clicks1, text='Ok', font="Times 10", padx="17", pady="3").place(x=60, y=128)
    tk.Button(Multiple_clicks1, text='Cancel', font="Times 10", padx="7", pady="3", command=Multiple_clicks1.destroy).place(x=163, y=128)


def Hotkey():
    Hotkey1 = tk.Toplevel()
    Hotkey1.title("Hotkey Setting")
    Hotkey1.geometry('230x110')
    Hotkey1.grab_set()
    Hotkey1.resizable(False, False)
    Hotkey1.attributes('-topmost', 1)
    Hotkey1.protocol("WM_DELETE_WINDOW", disable_x)
    tk.Button(Hotkey1, text='Click/Stop', font="Times 10", padx="18", pady="3").place(x=11, y=18)
    tk.Button(Hotkey1, text='F8', font="Times 10", padx="39", pady="3").place(x=120, y=18)  # переделать текст
    tk.Button(Hotkey1, text='Ok', font="Times 10", padx="17", pady="3").place(x=40, y=65)
    tk.Button(Hotkey1, text='Cancel', font="Times 10", padx="7", pady="3", command=Hotkey1.destroy).place(x=130, y=65)


def View():
    View1 = tk.Toplevel()
    View1.title("View Setting")
    View1.geometry("280x145")
    View1.grab_set()
    View1.resizable(False, False)
    View1.attributes('-topmost', 1)
    View1.protocol("WM_DELETE_WINDOW", disable_x)
    tk.Checkbutton(View1, text="Hide when it is clicking", onvalue=1, offvalue=0).place(x=10, y=10)  # переделать
    tk.Checkbutton(View1, text="Show when it finish clik", onvalue=1, offvalue=0).place(x=10, y=80)  # переделать
    tk.Button(View1, text='Ok', font="Times 10", padx="17", pady="3").place(x=56, y=134)  # переделать
    tk.Button(View1, text='Cancel', font="Times 10", padx="7", pady="3", command=View1.destroy).place(x=148, y=134)  # переделать


def Other():
    Other1 = tk.Toplevel()
    Other1.title("Other Setting")
    Other1.geometry("252x170")
    Other1.grab_set()
    Other1.resizable(False, False)
    Other1.attributes('-topmost', 1)
    Other1.protocol("WM_DELETE_WINDOW", disable_x)
    frame = tk.LabelFrame(Other1, text='On click complete', padx="80", pady="19")   # переделать
    frame.place(x=5, y=6)                                     # переделать
    Combobox(frame, values=('Idle', 'Quit', 'Lock computer', 'Log off computer', 'Tum off computer', 'Standby', 'Hibemate (only if supported)'), state="readonly", width=15).grid(row=0, column=0)  # переделать
    tk.Checkbutton(Other1, text="Display balloon tip", onvalue=1, offvalue=0).place(x=10, y=85)  # переделать
    tk.Button(Other1, text='Ok', font="Times 10", padx="17", pady="3").place(x=56, y=130)  # переделать
    tk.Button(Other1, text='Cancel', font="Times 10", padx="7", pady="3", command=Other1.destroy).place(x=148, y=130)  # переделать


def link():
    webbrowser.open_new(r"https://github.com/A1exTrask/Python3_AutoClicker")


def About():
    messagebox.showinfo(title='About', message='Auto Clicker \n \n Version 1.0', icon='info')


def show_window(icon):
    icon.stop()
    root.after(0, root.deiconify)


def quit_window(icon):
    icon.stop()
    root.quit()


def withdraw_window():  # Исправить клик в свернутом состоянии
    root.withdraw()
    icon = Icon('main', Image.open('1.ico'), 'Auto Clicker',
                menu=Menu(MenuItem('Show', show_window), MenuItem('Exit', quit_window)))
    icon.run()


root = tk.Tk()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.geometry('230x110')
root.title('Auto Clicker')
root.resizable(False, False)
root.attributes('-topmost', 1)
root.protocol("WM_DELETE_WINDOW", withdraw_window)

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
Help_menu.add_command(label="How to automate a sequence of mouse clicks and keystrokes", command=link)
Help_menu.add_command(label="About", command=About)

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Options", menu=Options_menu)
main_menu.add_cascade(label="Help", menu=Help_menu)

root.config(menu=main_menu)

keyboard.add_hotkey("f8", callback)  # кнопка
tk.Button(root, text='Press F8 to click', padx="53", pady="5", cursor="hand2", command=callback).place(x=15, y=12)
tk.Button(root, text="Help >>", padx="72", pady="5", cursor="hand2", command=link).place(x=15, y=60)

root.mainloop()
