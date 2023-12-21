from tkinter import *
import string
import random


def clicked():
    btn.destroy()
    lbl.destroy()
    enter_number = str(txt.get())
    if len(enter_number) == 6 and enter_number.isdigit():
        letter1 = random.choice(string.ascii_uppercase)
        letter2 = random.choice(string.ascii_uppercase)
        letter3 = random.choice(string.ascii_uppercase)
        letter4 = random.choice(string.ascii_uppercase)
        first_module = enter_number[3] + enter_number[4] + enter_number[5] + letter1 + letter2
        second_module = enter_number[0] + enter_number[1] + enter_number[2] + letter3 + letter4
        third_module = str(int(enter_number[3] + enter_number[4] + enter_number[5]) + \
                           int(enter_number[0] + enter_number[1] + enter_number[2]))
        if len(third_module) < 4:
            third_module = '0' + third_module
        key = first_module + '-' + second_module + ' ' + third_module
        lb = Label(window, text=key, font=("Calibri", 24))
        lb.grid(column=1, row=0)
        txt.destroy()
    else:
        lb = Label(window, text="Введено неправильное значение", font=("Calibri", 24))
        lb.grid(column=1, row=0)
        txt.destroy()


window = Tk()
window.title('Homescapes key')

window.geometry("1200x630")
bg = PhotoImage(file="back.png")
label1 = Label(window, image=bg)
label1.place(x=0, y=0)

lbl = Label(window, text="Введите DEC-число из 6 знаков.",\
            font = ("Calibri", 24))
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=2, row=0)

btn = Button(window, text="enter", command=clicked)
btn.grid(column=3, row=0)

window.mainloop()