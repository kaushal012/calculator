from tkinter import *

root = Tk()
root.title("Simple calculator")
#input
e = Entry(root, width=45, borderwidth= 5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#funct
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number) )

def clearfunc():
    e.delete(0, END)



def addition():
    num = e.get()
    global f_num
    f_num = int(num)
    e.delete(0, END)
    global mat
    mat = "addition"

def subtraction():
    num = e.get()
    global f_num
    f_num = int(num)
    global mat
    mat = "sub"
    e.delete(0, END)

def multiplication():
    num = e.get()
    global f_num
    f_num= int(num)
    global mat
    mat = "mul"
    e.delete(0, END)

def division():
    num = e.get()
    global f_num
    f_num = int(num)
    global mat
    mat = "div"
    e.delete(0, END)

def square():
    num=e.get()
    e.delete(0,END)
    e.insert(0, int(num) * int(num))


def equalbut():
    sec_num = e.get()
    e.delete(0, END)
    if mat== "addition":
        e.insert(0, f_num + int(sec_num))
    elif mat=="sub":
        e.insert(0, f_num - int(sec_num))
    elif mat=="mul":
        e.insert(0, f_num * int(sec_num))
    elif mat=="div":
        e.insert(0, f_num / int(sec_num))
    



#buttons
button_1 = Button(root, text="1", padx=25, pady=25 ,command= lambda: button_click(1))
button_2 = Button(root, text="2", padx=25, pady=25 ,command= lambda: button_click(2))
button_3 = Button(root, text="3", padx=25, pady=25 ,command= lambda: button_click(3))
button_4 = Button(root, text="4", padx=25, pady=25 ,command= lambda: button_click(4))
button_5 = Button(root, text="5", padx=25, pady=25 ,command= lambda: button_click(5))
button_6 = Button(root, text="6", padx=25, pady=25 ,command= lambda: button_click(6))
button_7 = Button(root, text="7", padx=25, pady=25 ,command= lambda: button_click(7))
button_8 = Button(root, text="8", padx=25, pady=25 ,command= lambda: button_click(8))
button_9 = Button(root, text="9", padx=25, pady=25 ,command= lambda: button_click(9))
button_0 = Button(root, text="0", padx=25, pady=25 ,command= lambda: button_click(0))
button_equal = Button(root, text="=", padx=25, pady=25, command= equalbut)
button_clr = Button(root, text="CLR", padx=25, pady=25, command=clearfunc)
button_mul = Button(root, text="*", padx=25, pady=25, command= multiplication)
button_div = Button(root, text="/", padx=25, pady=25, command= division)
button_sub = Button(root, text="-", padx=25, pady=25, command= subtraction)
button_add = Button(root, text="+", padx=25, pady=25, command= addition)
button_squ = Button(root, text="^2", padx = 20, pady=20, command= square)



#buttons on screen
button_1.grid(row=3 , column=0)
button_2.grid(row=3 , column=1)
button_3.grid(row=3 , column=2)

button_4.grid(row=2 , column=0)
button_5.grid(row=2 , column=1)
button_6.grid(row=2 , column=2)

button_7.grid(row=1 , column=0)
button_8.grid(row=1 , column=1)
button_9.grid(row=1 , column=2)

button_0.grid(row=4 , column=0)

button_div.grid(row=1 , column=3, columnspan=1)
button_mul.grid(row=2 , column=3)
button_sub.grid(row=3 , column=3)
button_add.grid(row=4 , column=3)

button_clr.grid(row=4 , column=1)
button_equal.grid(row=4 , column=2)
button_squ.grid(row=0, column=3)



root.mainloop()
