import random
from tkinter import *
import string

def create_password():
    password = []
    for i in range (5):
        alpha =random.choice(string.ascii_letters) #picks a letter
        symbol = random.choice(string.punctuation) #picks a symbol
        number = random.choice(string.digits) #picks a number

        password.append(alpha)
        password.append(symbol)
        password.append(number)

    y = "".join(str(x) for x in password)
    lbl.config(text=y)


root = Tk()
root.title("PASSWORD GENERATOR")
root.geometry("360X300")

btn = Button(root, text="Create Password", command= create_password)
btn.grid(row = 2, column = 2)

lbl = Label(root, font=("times", 15, "bold"))
lbl.grid(row= 4, column= 2)


root.mainloop()


