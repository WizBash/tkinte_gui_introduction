from tkinter import *
import tkinter as tk

def text_changed(*args):
    print("Text changed.")

top = tk.Tk()

string_listener = StringVar()
string_listener.set("")
string_listener.trace("w", text_changed)

entry_widget = tk.Entry(top, textvariable = string_listener)
entry_widget.pack()

top.mainloop()
