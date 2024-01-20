from tkinter import*
from tkinter import messagebox
def login():
    messagebox.showinfo("data")
    

    
hi=Tk()
hi.title("userdata")
Label(hi,text="name").place(x=20,y=20)
name=Entry(hi,bd=1).place(x=120,y=15)
Button(hi,text="click",command=login,bd=7).place(x=200,y=200)
hi.mainloop


             
