from tkinter import *
import pandas as pd 

import backend1

#working on dump
selected_tuple = None
def get_selected_row(event):
    try:
        global selected_tuple
        index=listbox.curselection()[0]
        selected_tuple=listbox.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[0])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[1])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[2])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[3])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[4])
    except IndexError:
        pass 

def view_command():
    listbox.delete(0,END)
    
    #listbox.insert(END,"\n")
    for items in backend1.view():
        
        listbox.insert(END,items)

def insert():
    if(product_id.get()=="" or date_from.get()=="" or date_to.get()=="" or amount.get()=="" or price_info.get()==""):
        pass
    else:
        
        backend1.insert(product_id.get(),date_from.get(),date_to.get(),amount.get(),price_info.get())
        listbox.delete(0,END)
        listbox.insert(END,(product_id.get(),date_from.get(),date_to.get(),amount.get(),price_info.get()))


def update():
    backend1.update(product_id.get(),date_from.get(),date_to.get(),amount.get(),price_info.get())
def delete():
    backend1.delete(selected_tuple[0])

def search_command():
    listbox.delete(0,END)
    for row in backend1.search(product_id.get(),date_from.get(),date_to.get(),amount.get(),price_info.get()):
        listbox.insert(END,row)

    
window=Tk()
frame1=Frame(window)
frame1.pack()
    
l1=Label(frame1,text="enter productID",font="Times 12 bold",width=12)
l1.grid(row=0,column=0)
l2=Label(frame1,text="enter date_from",font="Times 12 bold",width=12)
l2.grid(row=0,column=2)
l3=Label(frame1,text="enter date_to",font="Times 12 bold",width=12)
l3.grid(row=1,column=0)
l4=Label(frame1,text="amount",font="Times 12 bold",width=12)
l4.grid(row=1,column=2)
l5=Label(frame1,text="price info",font="Times 12 bold",width=12)
l5.grid(row=2,column=0)

product_id=StringVar()
e1=Entry(frame1,width=30,textvariable=product_id)
e1.grid(row=0,column=1)
date_from=StringVar()
e2=Entry(frame1,width=30,textvariable=date_from)
e2.grid(row=0,column=3)
date_to=StringVar()
e3=Entry(frame1,width=30,textvariable=date_to)
e3.grid(row=1,column=1)
amount=StringVar()
e4=Entry(frame1,width=30,textvariable=amount)
e4.grid(row=1,column=3)
price_info=StringVar()
e5=Entry(frame1,width=30,textvariable=price_info)
e5.grid(row=2,column=1)

frame2 = Frame(window)       
frame2.pack()

b1=Button(frame2,text="Viewall",font="Times 12",width=9,command=view_command)
b1.grid(row=4,column=0)
b2=Button(frame2,text="Insert",font="Times 12",width=9,command=insert)
b2.grid(row=4,column=1)
b3=Button(frame2,text="Update",font="Times 12",width=9,command=update)
b3.grid(row=4,column=2)
b3=Button(frame2,text="Search",font="Times 12",width=9,command=search_command)
b3.grid(row=4,column=3)
b4=Button(frame2,text="Delete",font="Times 12",width=9,command=delete)
b4.grid(row=4,column=4)
b5=Button(frame2,text="Close",font="Times 12",width=9,command=window.destroy)
b5.grid(row=4,column=5)

frame3 = Frame(window)       
frame3.pack()
scroll = Scrollbar(frame3, orient=VERTICAL)
listbox= Listbox(frame3, yscrollcommand=scroll.set,width=80,height=16)
scroll.config(command=listbox.yview)
scroll.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
listbox.bind('<<ListboxSelect>>',get_selected_row)
    
window.mainloop()