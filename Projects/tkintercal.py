from tkinter import *
from tkinter import ttk

LARGE_FONT = ('Verdana', 12)


def quit():
    sys.exit()


class MainApp(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, 'Client')
        Tk.wm_geometry(self, '200x200')

        container = ttk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in(StartPage, PageOne, PageTwo, PageThree, PageFour):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='NSEW')

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller,):
        Frame.__init__(self, parent)
        label = Label(self, text='Start Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text='Adunare', command=lambda: controller.show_frame(PageOne))
        button.pack()

        button1 = ttk.Button(self, text='Scadere', command=lambda: controller.show_frame(PageTwo))
        button1.pack()

        button2 = ttk.Button(self, text='Inmultire', command=lambda: controller.show_frame(PageThree))
        button2.pack()

        button3 = ttk.Button(self, text='Impartire', command=lambda: controller.show_frame(PageFour))
        button3.pack()

        label1 = Label(self, text='---------------')
        label1.pack()

        button4 = ttk.Button(self, text='Quit', command=quit)
        button4.pack()


class PageOne(Frame):

        def __init__(self, parent, controller,):
            Frame.__init__(self, parent)
            label = Label(self, text='Adunare', font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            def on_entry_click(event):
                """function that gets called whenever entry is clicked"""
                if entry1.get() == 'Introdu un numar':
                    entry1.delete(0, "end")  # delete all the text in the entry
                    entry1.insert(0, '')  # Insert blank for user input
                    entry1.config(fg='black')

            def on_entry_click1(event):
                if entry2.get() == 'Introdu un numar':
                    entry2.delete(0, "end")  # delete all the text in the entry
                    entry2.insert(0, '')  # Insert blank for user input
                    entry2.config(fg='black')

            def on_focusout(event):
                if entry1.get() == '':
                    entry1.insert(0, 'Introdu un numar')
                    entry1.config(fg='grey')

            def on_focusout1(event):
                if entry2.get() == '':
                    entry2.insert(0, 'Introdu un numar')
                    entry2.config(fg='grey')

            entry1 = Entry(self, bd=1)
            entry1.insert(0, 'Introdu un numar')
            entry1.bind('<FocusIn>', on_entry_click)
            entry1.bind('<FocusOut>', on_focusout)
            entry1.config(fg='grey')
            entry1.pack()
            entry1.pack()

            entry2 = Entry(self, bd=1)
            entry2.insert(0, 'Introdu un numar')
            entry2.bind('<FocusIn>', on_entry_click1)
            entry2.bind('<FocusOut>', on_focusout1)
            entry2.config(fg='grey')
            entry2.pack()

            rezultat = Label(self)

            def operatie():
                x = int(entry1.get())
                y = int(entry2.get())
                r = x + y
                rezultat['text'] = 'Rezultatul este  ' + str(r)

            def clear_text():
                entry1.delete(0, 'end')
                entry2.delete(0, 'end')

            button3 = ttk.Button(self, text='Pagina de start', command=lambda: [controller.show_frame(StartPage),
                                                                                clear_text()])
            button3.pack()

            button4 = ttk.Button(self, text='Egal', command=operatie)
            button4.pack()

            rezultat.pack()


class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label2 = Label(self, text='Scadere', font=LARGE_FONT)
        label2.pack(padx=10, pady=10)

        def on_entry_click(event):
            """function that gets called whenever entry is clicked"""
            if entry1.get() == 'Introdu un numar':
                entry1.delete(0, "end")  # delete all the text in the entry
                entry1.insert(0, '')  # Insert blank for user input
                entry1.config(fg='black')

        def on_entry_click1(event):
            if entry2.get() == 'Introdu un numar':
                entry2.delete(0, "end")  # delete all the text in the entry
                entry2.insert(0, '')  # Insert blank for user input
                entry2.config(fg='black')

        def on_focusout(event):
            if entry1.get() == '':
                entry1.insert(0, 'Introdu un numar')
                entry1.config(fg='grey')

        def on_focusout1(event):
            if entry2.get() == '':
                entry2.insert(0, 'Introdu un numar')
                entry2.config(fg='grey')

        entry1 = Entry(self, bd=1)
        entry1.insert(0, 'Introdu un numar')
        entry1.bind('<FocusIn>', on_entry_click)
        entry1.bind('<FocusOut>', on_focusout)
        entry1.config(fg='grey')
        entry1.pack()
        entry1.pack()

        entry2 = Entry(self, bd=1)
        entry2.insert(0, 'Introdu un numar')
        entry2.bind('<FocusIn>', on_entry_click1)
        entry2.bind('<FocusOut>', on_focusout1)
        entry2.config(fg='grey')
        entry2.pack()

        rezultat = Label(self)

        def operatie():
            x = int(entry1.get())
            y = int(entry2.get())
            r = x - y
            rezultat['text'] = 'Rezultatul este  ' + str(r)

        def clear_text():
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')

        button5 = ttk.Button(self, text='Pagina de start', command=lambda: [controller.show_frame(StartPage),
                                                                            clear_text()])
        button5.pack()

        button6 = ttk.Button(self, text='Egal', command=operatie)
        button6.pack()

        rezultat.pack()


class PageThree(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label2 = Label(self, text='Inmultire', font=LARGE_FONT)
        label2.grid(row=1, column=0, padx=65, pady=10)

        def on_entry_click(event):
            """function that gets called whenever entry is clicked"""
            if entry1.get() == 'Introdu un numar':
                entry1.delete(0, "end")  # delete all the text in the entry
                entry1.insert(0, '')  # Insert blank for user input
                entry1.config(fg='black')

        def on_entry_click1(event):
            if entry2.get() == 'Introdu un numar':
                entry2.delete(0, "end")  # delete all the text in the entry
                entry2.insert(0, '')  # Insert blank for user input
                entry2.config(fg='black')

        def on_focusout(event):
            if entry1.get() == '':
                entry1.insert(0, 'Introdu primul numar')
                entry1.config(fg='grey')

        def on_focusout1(event):
            if entry2.get() == '':
                entry2.insert(0, 'Introdu al doilea numar')
                entry2.config(fg='grey')

        entry1 = Entry(self, bd=1)
        entry1.insert(0, 'Introdu un numar')
        entry1.bind('<FocusIn>', on_entry_click)
        entry1.bind('<FocusOut>', on_focusout)
        entry1.config(fg='grey')
        entry1.grid(row=2, column=0)

        entry2 = Entry(self, bd=1)
        entry2.insert(0, 'Introdu un numar')
        entry2.bind('<FocusIn>', on_entry_click1)
        entry2.bind('<FocusOut>', on_focusout1)
        entry2.config(fg='grey')
        entry2.grid(row=3, column=0)

        rezultat = Label(self)

        def operatie():
            x = int(entry1.get())
            y = int(entry2.get())
            r = x * y
            rezultat['text'] = 'Rezultatul este  ' + str(r)

        def clear_text():
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')

        button5 = ttk.Button(self, text='Pagina de start', command=lambda: [controller.show_frame(StartPage),
                                                                            clear_text()])
        button5.grid(row=4, column=0)

        button6 = ttk.Button(self, text='Egal', command=operatie)
        button6.grid(row=5, column=0)

        rezultat.grid(row=7, column=0)


class PageFour(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label2 = Label(self, text='Impartire', font=LARGE_FONT)
        label2.pack(padx=10, pady=10)

        def on_entry_click(event):
            """function that gets called whenever entry is clicked"""
            if entry1.get() == 'Introdu un numar':
                entry1.delete(0, "end")  # delete all the text in the entry
                entry1.insert(0, '')  # Insert blank for user input
                entry1.config(fg='black')

        def on_entry_click1(event):
            if entry2.get() == 'Introdu un numar':
                entry2.delete(0, "end")  # delete all the text in the entry
                entry2.insert(0, '')  # Insert blank for user input
                entry2.config(fg='black')

        def on_focusout(event):
            if entry1.get() == '':
                entry1.insert(0, 'Introdu un numar')
                entry1.config(fg='grey')

        def on_focusout1(event):
            if entry2.get() == '':
                entry2.insert(0, 'Introdu un numar')
                entry2.config(fg='grey')

        entry1 = Entry(self, bd=1)
        entry1.insert(0, 'Introdu un numar')
        entry1.bind('<FocusIn>', on_entry_click)
        entry1.bind('<FocusOut>', on_focusout)
        entry1.config(fg='grey')
        entry1.pack()
        entry1.pack()

        entry2 = Entry(self, bd=1)
        entry2.insert(0, 'Introdu un numar')
        entry2.bind('<FocusIn>', on_entry_click1)
        entry2.bind('<FocusOut>', on_focusout1)
        entry2.config(fg='grey')
        entry2.pack()

        rezultat = Label(self)

        def operatie():
            x = int(entry1.get())
            y = int(entry2.get())
            r = x / y
            rezultat['text'] = 'Rezultatul este  ' + str(r)

        def clear_text():
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')

        button5 = ttk.Button(self, text='Pagina de start', command=lambda: [controller.show_frame(StartPage),
                                                                            clear_text()])
        button5.pack()

        button6 = ttk.Button(self, text='Egal', command=operatie)
        button6.pack()

        rezultat.pack()


app = MainApp()

app.mainloop()
