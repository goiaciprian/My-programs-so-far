#!usr/bin/env python

import tkinter as tk


class MyApp(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('New model')
        self.root.geometry('300x200')

        tk.Frame.__init__(self, self.root)
        self.pack(fill=tk.X)
        self.create_widget()

    def create_widget(self):
        first_label = tk.Label(self, text='Da', bg='white')
        first_label.pack()

    def start(self):
        self.root.mainloop()


MyApp().start()
