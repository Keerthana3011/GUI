from tkinter import*
from tkinter import messagebox
def login():
    l=Tk()
    l.title("login")
    l.geometry("400x400")
    Label(l,text="username",height=2,width=12,bd=5).place(x=60,y=60)
    Label(l,text="password",height=2,width=12,bd=5).place(x=60,y=120)
    entry1=Entry(l,bd=6)
    entry1.place(x=140,y=60)
    entry2=Entry(l,bd=6)
    entry2.place(x=140,y=120)
    l.mainloop()

def signup():
    s=Tk()
    s.title("signup")
    s.geometry("400x400")
    Label(s,text="username",height=2,width=12,bd=5).place(x=60,y=60)
    Label(s,text="password",height=2,width=12,bd=5).place(x=60,y=120)
    Label(s,text="age",height=2,width=12,bd=5).place(x=60,y=180)
    entry3=Entry(s,bd=6)
    entry3.place(x=150,y=60)
    entry4=Entry(s,bd=6)
    entry4.place(x=150,y=120)
    entry5=Entry(s,bd=6)
    entry5.place(x=150,y=180)
    Button(hi,text="Submit",command=submit,bd=7).place(x=100,y=160)
    
    s.mainloop()
    

def submit():
    su=Tk()
    su.title("Submit")
    su.geometry("400x400")
    username=entry7.get()
    password=entry8.get()
    if(username==""and password==""):
        messagebox.showinfo("blankspace not allowed")
    else:
        messagebox.showinfo("next step")
   
    
    
    
    su.mainloop()
    

hi=Tk()
hi.title("sl")

hi.geometry("400x400")
Button(hi,text="Login",command=login,bd=7).place(x=20,y=20)
Button(hi,text="Signup",command=signup,bd=7).place(x=80,y=20)


hi.mainloop()



    
    
