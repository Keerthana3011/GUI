from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import csv

def login():
    f=open("jag.csv","r",newline="")
    s=csv.reader(f)
    username=entry1.get()
    password=entry2.get()
    found=0
    if (username=="" or password==""):
        messagebox.showinfo("error","blank")
    for i in s:
        if (username==i[0] and password==i[1]):
            messagebox.showinfo("success","loged in")
            found=1
            break
        if found==0:
            messagebox.showinfo("error","Invalid")
            f.close

def signup():
    r=Tk()
    r.title("signup")
    r.geometry("400x400")
    Label(r,text="Name").place(x=20,y=20)
    Label(r,text="password").place(x=20,y=100)
    Label(r,text="email").place(x=20,y=180)
    global name
    global password
    global email

    name=Entry(r,bd=5)
    name.place(x=150,y=20)
    password=Entry(r,bd=5)
    password.place(x=150,y=100)
    email=Entry(r,bd=5)
    email.place(x=150,y=180)
    Button(r,text="create",command=message).place(x=200,y=315)
    r.mainloop()


def message():
    n=name.get()
    p=password.get()
    e=email.get()
    if(n=="" or p=="" or e==""):
        messagebox.showinfo("error","not allowed")
    else:
        messagebox.showinfo("success","new acc")
        l=[n,p,e]
        f=open("jag.csv","a",newline="")
        s=csv.writer(f)
        s.writerow(l)
        f.close
               


def new():
    k=Tk()
    k.title("login page")
    k.geometry("300x300")
    Label(k,text="Username").place(x=20,y=20)
    Label(k,text="password").place(x=20,y=80)
    global entry1
    global entry2
    entry1=Entry(k,bd=5)
    entry1.place(x=100,y=20)
    entry2=Entry(k,bd=5)
    entry2.place(x=100,y=80)

    b=Button(k,text="Lofin",command=login)
    b.place(x=125,y=150)
    k.mainloop()

root2=Tk()
root2.geometry("300x170")
root2.title("hi")
Label(root2,text="choose yout type").pack()
Button(root2,text="Login",command=new).pack(side = LEFT,padx=20,pady=40)
Button(root2,text="signup",command=signup).pack(side = RIGHT,padx=50,pady=40)











    
    
    
