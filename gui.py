from tkinter import *
import finance

def show_command():
    finance.init((sym_data.get()).upper(),int(e_day.get()),int(e_mon.get()),int(e_year.get()),
    int(ex_day.get()),int(ex_mon.get()),int(ex_year.get()))
    finance.Plot(sym_data.get().upper())

def clear_entry(event):
    event.widget.delete(0, END)

window=Tk()
window.option_add("*Font", ("Courier", 12))
window.wm_title("Finance Graph Generator")
l1=Label(window,text="Enter Symbol:")
l1.grid(row=0,column=0,columnspan=4)

sym_data=StringVar()
e1=Entry(window,width=44,textvariable=sym_data)
e1.grid(row=1,column=0,columnspan=11)

l2=Label(window,text="From")
l2.grid(row=2,column=0,columnspan=5)

l3=Label(window,text="To")
l3.grid(row=2,column=6,columnspan=5)

e_day=StringVar()
e2=Entry(window,width=4,textvariable=e_day)
e2.grid(row=3,column=0)
e2.insert(0,"dd")
e2.bind('<FocusIn>',clear_entry)

l4=Label(window,text="/")
l4.grid(row=3,column=1)

e_mon=StringVar()
e3=Entry(window,width=4,textvariable=e_mon)
e3.grid(row=3,column=2)
e3.insert(0,"mm")
e3.bind('<FocusIn>',clear_entry)

l5=Label(window,text="/")
l5.grid(row=3,column=3)

e_year=StringVar()
e4=Entry(window,width=4,textvariable=e_year)
e4.grid(row=3,column=4)
e4.insert(0,"yyyy")
e4.bind('<FocusIn>',clear_entry)
##################################################################################
space_label=Label(window,text="\t")
space_label.grid(row=3,column=5)

ex_day=StringVar()
e5=Entry(window,width=4,textvariable=ex_day)
e5.grid(row=3,column=6)
e5.insert(0,"dd")
e5.bind('<FocusIn>',clear_entry)

l6=Label(window,text="/")
l6.grid(row=3,column=7)

ex_mon=StringVar()
e7=Entry(window,width=4,textvariable=ex_mon)
e7.grid(row=3,column=8)
e7.insert(0,"mm")
e7.bind('<FocusIn>',clear_entry)

l7=Label(window,text="/")
l7.grid(row=3,column=9)

ex_year=StringVar()
e8=Entry(window,width=4,textvariable=ex_year)
e8.grid(row=3,column=10)
e8.insert(0,"yyyy")
e8.bind('<FocusIn>',clear_entry)

window.option_add("*Font", ("Courier", 10))

b1=Button(window,width=20,text="Generate Graph",command=show_command)
b1.grid(row=4,column=0,columnspan=11)

b2=Button(window,width=20,text="Close",command=window.destroy)
b2.grid(row=6,column=0,columnspan=11)

window.mainloop()