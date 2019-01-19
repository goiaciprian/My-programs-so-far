from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from afterlogin import SampleApp


desktop = os.path.expanduser("~/Desktop/savefile.txt")


def login():
    global nume_entry
    global parola_entry
    global root_log_in

    root_log_in = Tk()

    root_log_in.title('Log in')

    first_label = Label(root_log_in, text='Logheza-te', font=30)
    first_label.grid(row=0, columnspan=2, padx=10, pady=10)

    nume_label = Label(root_log_in, text='Nume de utilizator:')
    nume_label.grid(row=1, column=0)

    parola_label = Label(root_log_in, text='Parola:')
    parola_label.grid(row=2, column=0, sticky=W)

    nume_entry = ttk.Entry(root_log_in)
    nume_entry.grid(row=1, column=1, padx=4, pady=2)

    parola_entry = ttk.Entry(root_log_in, show='*')
    parola_entry.grid(row=2, columnspan=2, padx=2, pady=5)

    log_in_button = ttk.Button(root_log_in, text='Log In', command=check)
    log_in_button.grid(row=3, column=0, pady=5, padx=5, sticky=W)

    sign_up_button = ttk.Button(root_log_in, text='Sign up', command=signup)
    sign_up_button.grid(row=3, columnspan=2)

    quit_button = ttk.Button(root_log_in, text='Exit', command=iesire)
    quit_button.grid(row=3, column=1, sticky=E, padx=5)

    root_log_in.mainloop()


def iesire():
    exit()


def check():
    try:
        with open(desktop, 'r') as svfile:
            content = svfile.read()
            if ' ' + nume_entry.get() + ' ' + parola_entry.get() in content:
                root_log_in.destroy()
                app = SampleApp()
                app.mainloop()
            else:
                messagebox.showerror('Eroare', 'Nu s-a gasit contul.')
    except FileNotFoundError:
        messagebox.showerror('Error', 'Fisierul nu exista')


def signup():
    with open(desktop, 'a') as svafile:
        if nume_entry.get() == '' and parola_entry.get() == '':
            messagebox.showerror('Eroare', 'Introdu numele si parola')
        elif nume_entry.get() == '' or parola_entry.get() == '':
            messagebox.showerror('Eroare', 'Introdu numele si parola')
        else:
            svafile.write(' ' + nume_entry.get() + ' ' + parola_entry.get())
            messagebox.showinfo('Sing up', 'Contul a fost creat cu success.')


if __name__ == '__main__':
    login()
