import tkinter as tk

root = tk.Tk()

class GUI(tk.Frame):
    def __init__(self, master=root):
        super(GUI, self).__init__(master)

        self.string_listener = tk.StringVar()
        self.string_listener.set("Init Text")
        self.string_listener.trace("w", self.text_changed_callback)

        entry_widget = tk.Entry(master, textvariable=self.string_listener)
        entry_widget.pack()

    def text_changed_callback(self, *args):
        print("Text changed.")

gui = GUI()
gui.mainloop()