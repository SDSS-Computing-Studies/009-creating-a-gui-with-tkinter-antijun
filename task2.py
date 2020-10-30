import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

dogp = PhotoImage(file="dog.png")

sbn = Button(window, text="Search By Name")
nEntry = Entry(window, text="1")

dog = Label(window, image=dogp)
cdb = Label(window, text="Client Database")

nameL = Label(window, text="Name")
typeL = Label(window, text="Type")
breedL = Label(window, text="Breed")
ownerL = Label(window, text="Owner")
bdayL = Label(window, text="Birthdate")

e1 = Entry(window, text="1")
e2 = Entry(window, text="2")
e3 = Entry(window, text="3")
e4 = Entry(window, text="4")
e5 = Entry(window, text="5")

pre = Button(window, text="< Previous")
save = Button(window, text="Save Entry")
nxt = Button(window, text="Next >")

# grid
dog.grid(row=1, column=1, rowspan=2)
cdb.grid(row=2, column=3)
sbn.grid(row=1, column=4)
nEntry.grid(row=1, column=5)

nameL.grid(row=4, column=1)
typeL.grid(row=4, column=2)
breedL.grid(row=4, column=3)
ownerL.grid(row=4, column=4)
bdayL.grid(row=4, column=5)

e1.grid(row=5, column=1)
e2.grid(row=5, column=2)
e3.grid(row=5, column=3)
e4.grid(row=5, column=4)
e5.grid(row=5, column=5)

pre.grid(row=6, column=1, rowspan=2)
save.grid(row=6, column=3)
nxt.grid(row=6, column=5)

window.mainloop()
