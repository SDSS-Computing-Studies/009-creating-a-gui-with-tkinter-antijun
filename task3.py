import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Example")

dogp = PhotoImage(file="dog.png")

l1 = Label(window, image=dogp)
l2 = Label(window, text="Pochacco!")
l3 = Label(window, text=" A cuddly little puppy! This is from the same ",
           background="#aaffff")
l4 = Label(window, text="creators who brought you Keropi and Kero Kero",
           background="#aaffff")

l1.grid(row=1, column=2, rowspan=3, columnspan=2)
l2.grid(row=2, column=3, columnspan=2)
l3.grid(row=4, column=2, columnspan=3)
l4.grid(row=5, column=2, columnspan=3)

window.mainloop()
