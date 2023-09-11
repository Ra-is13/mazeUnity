from tkinter import *
from tkinter import messagebox
import re
w=Tk()
w.geometry("530x200")

def me():
    choice1 = choice.get()
    print(choice1)
    r=E1.get()
    e=open(r,encoding="utf8")
    i=e.read()
    e.close()
    if choice1==1:
        a=re.findall("\d\d:\d\d:\d\d",i)
        print(a)
        messagebox.showinfo("ME",a)
    if choice1==2:
        a=re.findall("\s\d\d", i)
        messagebox.showinfo("ME",a)
    if choice1==3:
        a=re.findall("\D\D...\d\d", i)
        messagebox.showinfo("ME",a)

def delete():
    E1.delete(0,END)

choice = IntVar()
Label(w, text='Search pattern from the file and count the results').pack(pady=10)
f=Frame(w)
L1 = Label(f, text='Enter source file').grid(row=0,column=0)
E1 = Entry(f, bd=3, width=60)
E1.grid(row=0,column=2)
f.pack()

f1=Frame(w)
R1 = Radiobutton(f1, text="Pattern = \d\d:\d\d:\d\d",variable=choice,value=1).pack()
R2 = Radiobutton(f1, text="Pattern = \s\d\d              ",variable=choice,value=2 ).pack()
R3 = Radiobutton(f1, text="Pattern = \D\D...\d\d     ",variable=choice,value=3 ).pack()
f1.pack()
f2=Frame(w)
b1=Button(f2,text="Clear",width=8,height=1,fg="White",bg="DARKORCHID",command=delete)
b2=Button(f2,text="Ok",width=8,height=1,fg="White",bg="DARKORCHID",command=me)
b3=Button(f2,text="Cancel",width=8,height=1,fg="White",bg="DARKORCHID",command=w.destroy)
b1.grid(row=0,column=1,padx=40,pady=10)
b2.grid(row=0,column=2,padx=40,pady=10)
b3.grid(row=0,column=3,padx=40,pady=10)
f2.pack()
w.mainloop()
