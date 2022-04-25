from tkinter import *

root = Tk()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.title('Click counter')
root.geometry('180x130')
root.resizable(width=False, height=False)
root.attributes('-topmost', 1)

count = 0


def clicked():
    global count
    count += 1
    Click.configure(text=count)


Click = Label(root, text='0', font='Arial 35')
Click.pack()

btn = Button(root, text='Click on me', padx='20', pady='20', cursor="hand2", command=clicked)
btn.pack()

root.mainloop()
