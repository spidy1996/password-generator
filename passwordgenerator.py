import random, string
from tkinter import *


def passgen():
    e3.delete('1.0', END)
    l = int(e1.get())
    password = ""
    for i in range(l):
        password += string.printable[random.randint(0, 94)]
    e3.insert(END, password)


root = Tk()
l1 = Label(root, text="Enter the length of password : ")
e1 = Entry(root)
b1 = Button(root, text="Generate!", command=passgen)
l2 = Label(root, text="PASSWORD GENERATOR")
l3 = Label(root, text="Generated Password is : ")
e3 = Text(root, width=20, height=5)


l2.grid(row=0, columnspan=2)
l1.grid(row=1, column=0)
e1.grid(row=1, column=1)
b1.grid(row=2, columnspan=2)
l3.grid(row=3, column=0)
e3.grid(row=3, column=1)
root.mainloop()
