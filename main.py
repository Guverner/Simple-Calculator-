from tkinter import *

root= Tk()

root.title("Calculator")

def button_click(n):
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current)  +str(n))


def button_clear():
    e.delete(0 , END)


def button_add():
    firstn=e.get()
    global f_num
    global math
    math ="addition"
    f_num = int(firstn)
    e.delete(0, END)


def porcentage():
    firstn = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "procentage"
    f_num = int(firstn)
    e.delete(0, END )


def button_subtract():
    firstn= e.get()
    global f_num
    global math
    math= "subtract"
    f_num= int(firstn)
    e.delete(0,END)

def button_devide():
    firstn = e.get()
    global f_num
    global math
    math = "devide"
    f_num= int(firstn)
    e.delete(0, END)

def multyply():
    firstn=e.get()
    global f_num
    global math
    f_num= firstn
    math = "multiply"
    e.delete(0, END)

def button_equal():
    second_number= e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtract":
        e.insert(0, f_num - int(second_number))
    if math == "devide":
        e.insert(0, f_num / int(second_number))
    if math == "multiply":
        e.insert(0, f_num * int(second_number))
    if math == "procentage":
        e.insert(0, f_num / 100 * int(second_number))









e=Entry(width= 35, borderwidth= 1)
e.grid(row=0, column=0,columnspan=3, padx=10, pady=10 )


button1= Button(root, text= 1, padx=40, pady=20 , command=lambda: button_click(1))
button1.grid(row=3, column=2)

button2= Button(root, text=2, padx=40, pady=20,command=lambda: button_click(2))
button2.grid(row=3, column=1)


button3=Button(root, text=3, padx=40, pady=20,command=lambda: button_click(3))
button3.grid(row=3, column=0)

button4=Button(root, text=4, padx=40, pady=20,command=lambda: button_click(4))
button4.grid(row=2, column=2)

button5=Button(root, text=5, padx=40, pady=20,command=lambda: button_click(5))
button5.grid(row=2, column=1)

button6=Button(root, text=6, padx=40, pady=20,command=lambda: button_click(6))
button6.grid(row=2, column=0)

button7=Button(root, text=7, padx=40, pady=20,command=lambda: button_click(7))
button7.grid(row=1, column=2, )

button8=Button(root, text=8, padx=40, pady=20,command=lambda: button_click(8))
button8.grid(row=1, column=1 )

button9=Button(root, text=9, padx=40, pady=20,command=lambda: button_click(9))
button9.grid(row=1, column=0)

button0=Button(root, text=0, padx=40, pady=19,command=lambda: button_click(0))
button0.grid(row=4, column=0)

button_subtract=Button(root, text= "-", padx=40, pady=20, command=button_subtract)
button_subtract.grid(row=4, column=2)

button_devide=Button(root, text="/", padx=40, pady=19, command=button_devide)
button_devide.grid(row=5, column=1)

button_multiply = Button(root, text="*", padx=40, pady=20, command=multyply)
button_multiply.grid(row=5, column=0)

button_add=Button(root, text="+", padx=38, pady=19, command=button_add)
button_add.grid(row=4, column=1)

button_equal=Button(root, text= "=", padx= 37, pady=18, command=button_equal)
button_equal.grid(row= 5, column=2)

button_procentage = Button(root, text="%", padx= 40, pady=20, command=porcentage)
button_procentage.grid(row=6, column=1)

button_clear= Button(root, text="ERASE", padx=23, pady=20, command=button_clear)
button_clear.grid(row= 6, column=0)



root.mainloop()