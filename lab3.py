from tkinter import *
import string
import random

def clicked():
    btn.destroy()
    lbl.destroy()
    y = str(txt.get())
    letter1, letter2,letter3,letter4 = random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase)
    first_module = y[3] + y[4] + y[5] + letter1 + letter2
    second_module = y[0] + y[1] + y[2] + letter3 + letter4
    third_module = str(int(y[3] + y[4] + y[5]) + int(y[0] + y[1] + y[2]))
    if len(third_module)<4:
        third_module = '0' + third_module
    key = first_module + '-' + second_module + ' ' + third_module
    lb = Label(window, text=key, font=("Calibri", 24))
    lb.grid(column=1, row=0)
    txt.destroy()


window = Tk()
window.title('Homescapes key')

window.geometry("1200x630")
bg = PhotoImage(file = "back.png")
label1 = Label(window, image=bg)
label1.place(x=0, y=0)

lbl = Label(window, text="Введите DEC-число из 6 знаков.", font=("Calibri", 24))
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=2, row=0)

btn = Button(window, text="enter", command=clicked)
btn.grid(column=3, row=0)

window.mainloop()