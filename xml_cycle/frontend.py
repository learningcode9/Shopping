from tkinter import *
import pandas as pd 
import backend
import psycopg2
import lxml.etree as etree
import os.path
from os import path

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
    for items in backend.view():
       listbox.insert(END,' ',items)

def insert():
    if(product_id.get()=="" or date_from.get()=="" or date_to.get()=="" or amount.get()=="" or price_info.get()==""):
        pass
    else:
        backend.insert(product_id.get(),date_from.get(),date_to.get(),amount.get(),price_info.get())
        listbox.delete(0,END)
        listbox.insert(END,(product_id.get(),date_from.get(),date_to.get(),amount.get(),price_info.get()))

def update():
    backend.update(product_id.get(),date_from.get(),date_to.get(),amount.get(),price_info.get())
    listbox.delete(0,END)
    listbox.insert(END,'Data updated')
def delete():
    backend.delete(selected_tuple[0])
def search_command():
    listbox.delete(0,END)
    for row in backend.search(product_id.get(),date_from.get(),date_to.get(),amount.get(),price_info.get()):
        listbox.insert(END,' ',row)
data1="""<pricebooks xmlns="http://www.demandware.com/xml/impex/pricebook/2006-10-31">
	<pricebook>
		<header pricebook-id="belk-best-prices-usd">
			<currency>USD</currency>
			<display-name xml:lang="x-default">Best Price</display-name>
			<description xml:lang="x-default">Best Price</description>
			<online-flag>true</online-flag>
			<parent>belk-regular-prices-usd</parent>
		</header>"""
def dump_command():
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres1984'")
    except:
        print (" ***  Can't able to connect database. *** ")
        return False
    
    with open('data.xml', 'w') as outfile:
        cursor  = conn.cursor()
        cursor.execute("select * from  xmldatatable")
        rows = cursor.fetchall()
        outfile.write('<?xml version="1.0" encoding="UTF-8?>\n')
        outfile.write(data1)
        outfile.write("\n")
        outfile.write(' <price-tables>\n')
        for row in rows:
            outfile.write('  <price-table product-id="%s">\n' %(row[0]))
            outfile.write('     <online-from>%s</online-from>\n' % (row[1]))
            outfile.write('     <online-to>%s</online-to>\n' % (row[2]))
            outfile.write('     <amount quantity="1">%s</amount>\n' % (row[3]))
            outfile.write('     <price-info>%s</priceinfo>\n' % (row[4]))
            outfile.write('  </price-table>\n\n')
        outfile.write('     </price-tables>\n')
        outfile.write('    </pricebook>\n')
        outfile.write('</pricebooks>\n')
        outfile.close()
    if path.isfile('data.xml'):
        listbox.delete(0,END)
        listbox.insert(END,'File generated')
    else:
        listbox.delete(0,END)
        listbox.insert(END,'File is not generated')


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
b5=Button(frame2,text="Dump",font="Times 12",width=9,command=dump_command)
b5.grid(row=4,column=6)

frame3 = Frame(window)       
frame3.pack()
scroll = Scrollbar(frame3, orient=VERTICAL)
listbox= Listbox(frame3, yscrollcommand=scroll.set,width=80,height=16)
scroll.config(command=listbox.yview)
scroll.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
listbox.bind('<<ListboxSelect>>',get_selected_row)
    
window.mainloop()