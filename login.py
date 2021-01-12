from tkinter import*
from tkinter import ttk







root=Tk()
root.title('My Login Form')
root.config(bg='lightblue')

#=====================starting widgets=======================
frame1=Frame(root,bg='lightblue')
frame1.grid(row=1,column=1,columnspan=3,sticky='nw')
l1=Label(frame1,text='My Log In Form',bg='lightblue',fg='green',font=('times',25))
l1.grid(row=1,column=1,padx=10,pady=10)

frame2=Frame(root,bg='lightblue')
frame2.grid(row=2,column=1)
l2=Label(frame2,text='''Choose Your Account
And Log In
	''',fg='green',bg='lightblue',font=('times',15))
l2.grid(row=1,column=1)


mainloop()
