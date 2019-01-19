#!usr/bin/env python

from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title('merge')
        self.configure(background='white')

        container = Frame(
            self,
            background='white'
        )
        container.pack()

        title = ttk.Label(
            container,
            text='Mai stiu?',
            font='Halvatica 18 bold',
            background='white'
        )
        title.grid(
            row=0,
            column=0,
            columnspan=3,
            padx=10,
            pady=3
        )
        primul_rand = ttk.Label(
            container,
            font=23,
            text='Minute:',
            background='white'
        )
        primul_rand.grid(
            row=1,
            column=0,
            sticky=E
        )
        user_entry = ttk.Entry(
            container,
            width=10,
            justify=RIGHT
        )
        user_entry.grid(
            row=1,
            column=1,
            sticky=W,
            padx=5,
            pady=5
        )
        help_button = ttk.Button(
            container,
            text='?',
            width=3,
            command=lambda: print(user_entry.get())
        )
        help_button.grid(
            row=1,
            column=2,
            padx=3,
            pady=3,
            sticky=W
        )
        submit_button = ttk.Button(
            container,
            text='Submit',
            command=lambda: get(user_entry.get())
        )
        submit_button.grid(
            row=2,
            column=1,
            pady=3
        )

        def get(text_user):
            if text_user == '' or text_user == ' ':
                variabila = 0
                print(variabila)
            else:
                variabila = text_user
                print(variabila)

        self.mainloop()


if __name__ == '__main__':
    App()
