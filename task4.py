import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Example")
window.geometry("400x200")

dogp = PhotoImage(file="dog.png")

l1 = Label(window, image=dogp)
l2 = Label(window, text="Pochacco!")
l3 = Label(window, text=" A cuddly little puppy! This is from the same ",
           background="#aaffff")
l4 = Label(window, text="creators who brought you Keropi and Kero Kero",
           background="#aaffff")

l1.place(x=130, y=40)
l2.place(x=190, y=75)
l3.place(x=70, y=140)
l4.place(x=60, y=160)

window.mainloop()
