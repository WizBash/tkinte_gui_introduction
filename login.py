from tkinter import*
from tkinert import ttk







root=Tk()
root.title('My Login Form')
root.config(bg='green')

#=====================starting widgets=======================
frame1=Frame(root,bg='lightblue')
frame1.grid(row=1,column=1,columnspan=3,sticky='nw')
l1=Label(frame1,text='My Log In Form',bg='lightblue',fg='green',font=('times',15))
l1.grid(row=1,column=1,padx=10,pady=10)


mainloop()
