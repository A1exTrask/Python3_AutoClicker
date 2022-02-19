from tkinter import *

root = Tk()
root.title('Auto Clicker')
root.geometry('230x110')
root.resizable(width=False, height=False)

main_menu = Menu()
main_menu.add_cascade(label="File")
main_menu.add_cascade(label="Options")
main_menu.add_cascade(label="Help")

root.config(menu=main_menu)
root.mainloop()
