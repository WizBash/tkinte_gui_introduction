from tkinter import*
from tkinter import ttk







root=Tk()
root.title('My Login Form')
root.config(bg='lightblue')
root.geometry("500x300+400+300")
root.overrideredirect(True)
#=====================starting widgets=======================
frame1=Frame(root,bg='lightblue')
frame1.grid(row=1,column=1,columnspan=3,sticky='n',pady=10)
l1=Label(frame1,text='My Log In Form',bg='lightblue',fg='green',font=('times',25))
l1.grid(row=1,column=1,padx=10,pady=10)

frame2=Frame(root,bg='lightblue')
frame2.grid(row=2,column=1,sticky='n',pady=10,padx=10)
l2=Label(frame2,text='''Choose Your 
Account And 
Log In
	''',fg='green',bg='lightblue',font=('times',20))
l2.grid(row=1,column=1)

frame3=Frame(root,bg='white')
frame3.grid(row=2,column=2,sticky='ne',pady=10,padx=10)
l3=Label(frame3,text='User Name',font=('times',15),bg='white')
l3.grid(row=1,column=1,sticky='w',columnspan=2,padx=10)
user=Entry(frame3,width=25,font=('times',15),highlightthickness=1)
user.config(highlightbackground = "black")
user.grid(row=2,column=1,sticky='w',pady=10,columnspan=2,padx=10)
l3=Label(frame3,text='Passphrase',font=('times',15),bg='white')
l3.grid(row=3,column=1,sticky='w',columnspan=2,padx=10)
phrase=Entry(frame3,width=25,font=('times',15),highlightthickness=1,show='*')
phrase.config(highlightbackground = "black")
phrase.grid(row=4,column=1,sticky='w',pady=10,columnspan=2,padx=10)
ext=Button(frame3,text='EXIT',fg='black',bg='red',font=('times',13),width=15,command=quit)
ext.grid(row=5,column=1)
ext=Button(frame3,text='LOG IN',fg='black',bg='green',font=('times',13),width=15)
ext.grid(row=5,column=2)

mainloop()
#
#waiting for part two to develope functions
