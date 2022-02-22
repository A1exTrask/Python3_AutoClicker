from tkinter import *
from tkinter import messagebox
import webbrowser


def Exit():
    root.destroy()


def callback():
    webbrowser.open_new(r"https://github.com/A1exTrask/Python3_AutoClicker")


def About():
    messagebox.showinfo(title='About', message='Auto Clicker \n \n Version 1.0', icon='info')


def click():
    w


root = Tk()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.geometry('230x110')
root.title('Auto Clicker')
root.resizable(width=False, height=False)
root.attributes('-topmost', 1)

main_menu = Menu()

file_menu = Menu(tearoff=0)
file_menu.add_command(label="Exit", command=Exit)

Options_menu = Menu(tearoff=0)

Clicking_menu = Menu(Options_menu, tearoff=0)

Clicking_menu.add_command(label="Options")
Clicking_menu.add_command(label="Repeat")

Recording_menu = Menu(Options_menu, tearoff=0)

Recording_menu.add_command(label="Multiple clicks")

Settings_menu = Menu(Options_menu, tearoff=0)

Settings_menu.add_command(label="Hotkey")
Settings_menu.add_command(label="View")
Settings_menu.add_command(label="Other")

Options_menu.add_cascade(label="Clicking", menu=Clicking_menu)
Options_menu.add_cascade(label="Recording", menu=Recording_menu)
Options_menu.add_cascade(label="Settings", menu=Settings_menu)

Help_menu = Menu(tearoff=0)
Help_menu.add_command(label="How to automate a sequence of mouse clicks and keystrokes", command=callback)
Help_menu.add_command(label="About", command=About)

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Options", menu=Options_menu)
main_menu.add_cascade(label="Help", menu=Help_menu)

root.config(menu=main_menu)

m1 = Button(root, text='Press F8 to click', padx="53", pady="5", cursor="hand2", command=click)
m1.place(x=15, y=12)
m2 = Button(root, text="Help >>", padx="72", pady="5", cursor="hand2", command=callback)
m2.place(x=15, y=60)

root.mainloop()
