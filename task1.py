import tkinter as tk
from tkinter import *

window = tk.Tk()

f1 = Frame()

entry1 = Entry(f1, text="1", width=20)
mSign = Label(f1, text="x")
entry2 = Entry(f1, text="2", width=20)
eSign = Button(f1, text="=")
answer = Entry(f1, text="3", width=30)

f1.pack()

entry1.pack(side=LEFT)
mSign.pack(side=LEFT)
entry2.pack(side=LEFT)
eSign.pack(side=LEFT)
answer.pack(side=LEFT)

window.mainloop()
