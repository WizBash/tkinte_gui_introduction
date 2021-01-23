from tkinter import*
import time
import calendar
import random
import datetime



def now_time():
	hour=time.strftime('%I')
	minute=time.strftime('%M')
	second=time.strftime('%S')
	friday=time.strftime('%A')
	am=time.strftime('%p')
	zn=time.strftime('%Z')
	dy=time.strftime('%d')
	month=time.strftime('%B')
	yrrrr=time.strftime('%Y')


	labhour.config(text=hour)
	labmin.config(text=minute)
	labsec.config(text=second)
	strday.config(text=friday)
	labpm.config(text=am)
	zone.config(text=zn)
	labday.config(text=dy)
	strmonth.config(text=month)
	stryear.config(text=yrrrr)

	labsec.after(1000,now_time)






root=Tk()
frametime=Frame(root)
frametime.grid(row=1,column=1,sticky='nw',pady=10)

framedate=Frame(root)
framedate.grid(row=2,column=1,sticky='nw',pady=10)


zone=Label(frametime,text='',font=('times',15),fg='red')
zone.grid(row=0,column=1,columnspan=10,sticky='w',padx=5)

labhour=Label(frametime,text='',font=('times',20,'bold'),fg='red')
labhour.grid(row=1,column=1,sticky='w',padx=5)

labmin=Label(frametime,text='',font=('times',20,'bold'),fg='red')
labmin.grid(row=1,column=2,sticky='w',padx=5)

labsec=Label(frametime,text='',font=('times',20,'bold'),fg='red')
labsec.grid(row=1,column=3,sticky='w',padx=5)

labpm=Label(frametime,text='am',font=('times',20,'bold'),fg='red')
labpm.grid(row=1,column=4,sticky='w',padx=10)

strday=Label(framedate,text='Friday',font=('times',20),fg='red')
strday.grid(row=1,column=1,columnspan=5,sticky='w',padx=10)

labday=Label(framedate,text='00',font=('times',20,'bold'),fg='red')
labday.grid(row=2,column=1,sticky='w',padx=10)

strmonth=Label(framedate,text='January',font=('times',20,'bold'),fg='red')
strmonth.grid(row=2,column=2,sticky='w',padx=10)

stryear=Label(framedate,text='2001',font=('times',20,'bold'),fg='red')
stryear.grid(row=2,column=3,sticky='w',padx=10)

now_time()

mainloop()