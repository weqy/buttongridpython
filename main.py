import tkinter
from tkinter import messagebox

master = tkinter.Tk()
master.title("grid() method")
master.geometry("800x500")

z = 2000


def notify_me():
    messagebox.showinfo('python', 'hello world')


def which_button(button_press):
    messagebox.showinfo('python', 'you pressed ' + str(button_press))
    print(button_press)


for x in range(1, 11):
    for y in range(1, 11):
        button1 = tkinter.Button(master, text=z, command=lambda m=z: which_button(m))
        button1.grid(row=x, column=y)
        z += 1


master.mainloop()
