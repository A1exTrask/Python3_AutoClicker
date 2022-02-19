from tkinter import *


def Exit():
    root.destroy()


root = Tk()
root.title('Auto Clicker')
root.geometry('230x110')
root.resizable(width=False, height=False)

main_menu = Menu()

file_menu = Menu(tearoff=0)
file_menu.add_command(label="Exit", command=Exit)

Options_menu = Menu(tearoff=0)
Options_menu.add_command(label="Clicking")
Options_menu.add_command(label="Recording")
Options_menu.add_command(label="Settings")

Help_menu = Menu(tearoff=0)
Help_menu.add_command(label="About")

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Options", menu=Options_menu)
main_menu.add_cascade(label="Help", menu=Help_menu)

root.config(menu=main_menu)
root.mainloop()
