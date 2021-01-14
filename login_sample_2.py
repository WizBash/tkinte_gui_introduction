from tkinter import*
import sqlite3
import sys
from tkinter import ttk

#==================================== fees structure confirm form=============================
def liv():
	c_root.destroy()

def fee_structure():
	def be_enter(e):
		be['background'] = 'yellow'
	def be_leave(e):
		be['background'] = 'blue'
	def bl_enter(e):
		bl['background'] = 'yellow'
	def bl_leave(e):
		bl['background'] = 'blue'

	global c_root
	global c_pass
	c_root=Tk()
	c_root.title('Confirm User')
	c_root.overrideredirect(True) # removes the titile bar
	c_root.config(bg='white')
	c_root.resizable(0,0)
	#c_root.wm_attributes('-alpha',0.9) # makes transparent window
	#splash.wm_attributes('-topmost',True) #on top of all windows
	c_root.iconbitmap('icon.ico')
	c_root.geometry("300x210+550+300")
	c_frame1=Frame(c_root,bg='blueviolet')
	c_frame1.grid(row=1,column=1,stick='n')
	c_frame2=Frame(c_root,bg='white')
	c_frame2.grid(row=2,column=1,pady=22)
	c_frame3=Frame(c_root,bg='blueviolet')
	c_frame3.grid(row=3,column=1,sticky='s')

	l1=Label(c_frame1,text='Confirm User',font=('times',20),width=20,bg='blueviolet',fg='blue')
	l1.grid(row=1,column=1,pady=10)
	l1=Label(c_frame2,text='Insert Passphrase',font=('times',15),bg='white',fg='black')
	l1.grid(row=1,column=1)
	c_pass=Entry(c_frame2,width=25,font=('times',15),highlightthickness=1)
	c_pass.config(highlightbackground = "black")
	c_pass.grid(row=2,column=1)
	be=Button(c_frame3,text='Cancel',font=('times',15),width=13,bg='blue',fg='red',relief='raised',command=liv)
	be.grid(row=1,column=1,pady=10)
	bl=Button(c_frame3,text='Confirm',font=('times',15),width=13,bg='blue',fg='black',relief='raised')
	bl.grid(row=1,column=2,stick='e',pady=10)
	be.bind("<Enter>", be_enter)
	be.bind("<Leave>", be_leave)
	bl.bind("<Enter>", bl_enter)
	bl.bind("<Leave>", bl_leave)


	mainloop()
fee_structure()
