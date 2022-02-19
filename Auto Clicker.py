from tkinter import *

root = Tk()
root.title('Auto Clicker')
root.geometry('230x110')
root.resizable(width=False, height=False)

main_menu = Menu()

file_menu = Menu(tearoff=0)
file_menu.add_command(label="Exit")

Options_menu = Menu(tearoff=0)
Options_menu.add_command(label="1")
Options_menu.add_command(label="2")
Options_menu.add_command(label="3")

Help_menu = Menu(tearoff=0)
Help_menu.add_command(label="About")

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Options", menu=Options_menu)
main_menu.add_cascade(label="Help", menu=Help_menu)

root.config(menu=main_menu)
root.mainloop()
