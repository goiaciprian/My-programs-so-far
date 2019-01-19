import tkinter as tk
from tkinter import ttk


class Account:

    def __init__(self, balance=100):
        self.balance = balance

    def __str__(self):
        return f'Account balance: {self.balance}'

    def balance(self):
        return f'Aveti {self.balance} in cont'

    def deposit(self, suma):
        self.balance += suma
        return 'Deposit accepted'

    def withdraw(self, suma):
        if suma < self.balance:
            self.balance -= suma
            return 'Withdrow accepted'
        else:
            return 'Funds Unavailable!'


user = Account()


def iesire():
    exit()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Client')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Meniu", font=40)
        label.grid(row=0, columnspan=2, pady=10, padx=10)

        button1 = ttk.Button(self, text="Informatii", command=lambda: controller.show_frame("PageOne"))
        button2 = ttk.Button(self, text="Depune", command=lambda: controller.show_frame("PageTwo"))
        button1.grid(row=1, column=0, padx=5, pady=5)
        button2.grid(row=1, column=1, padx=5, pady=5)

        button3 = ttk.Button(self, text="Retrage", command=lambda: controller.show_frame("PageTwo"))
        button4 = ttk.Button(self, text="Iesire", command=iesire)

        button3.grid(row=2, column=0, padx=5, pady=5)
        button4.grid(row=2, column=1, padx=5, pady=5)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Informatii", font=50)
        label.grid(row=0, columnspan=1, pady=10, padx=10, sticky='E')
        info_label = tk.Label(self, text=f'{user}')
        info_label.grid(row=1, columnspan=2, sticky='E', padx=25)
        button = ttk.Button(self, text="Meniu", command=lambda: controller.show_frame("StartPage"))
        button.grid(row=2, columnspan=2, pady=10)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()
