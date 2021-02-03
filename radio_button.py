from tkinter import*

root = Tk()

v = StringVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [("Python", 'python'),
           ("Perl", 102),
           ("Java", 103),
             ("C++", 104),
             ("C", 105)]

def ShowChoice():
    print(v.get())

Label(root, 
         text="""Choose your favourite 
programming language:""",
         justify = LEFT,
         padx = 20).pack()

for language, val in languages:
    Radiobutton(root, 
                   text=language,
                   padx = 20, 
                   variable=v, 
                   command=ShowChoice,
                   value=val).pack(anchor=W)


root.mainloop()