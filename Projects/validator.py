#!usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import os


def resource_path(relative_path):
    """ Stabileste path-ul catre un folder temporar unde sunt incluse datele pt pyinstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class MyGui(tk.Tk):

    def __init__(self):

        tk.Tk.__init__(self)
        iconpath = resource_path('creditcard.ico')

        self.iconbitmap(iconpath)
        self.title('Client')
        self.eval(f"tk::PlaceWindow {self.winfo_toplevel()} center")
        self.geometry('230x129')
        self.resizable(False, False)
        self.config(bg='white')

        meniu = tk.Menu(self)

        def about_gui():

            mesaj = 'Acesta este un program care verifica doar\n autenticitatea codurilor cardurilor de credit.\n' \
                    'Nu preaia sau trimite informatii referitoare la\n card sau utilizator.\n' \
                    'Exemplu: 1234567891234567 sau\n 1234 5678 9123 4567.'

            _about = tk.Tk()

            _about.lift()
            _about.attributes('-topmost', True)
            _about.focus_force()

            _about.iconbitmap(iconpath)

            _about.title('About')
            _about.resizable(False, False)
            _about.config(bg='white')

            label_titlu = ttk.Label(
                _about,
                text='Ajutor : ',
                font='Times 18 bold italic',
                background='white'
            )

            label_titlu.pack()

            infolabel = ttk.Label(
                _about,
                text=mesaj,
                background='white',
                font='Times 14'

            )
            infolabel.pack(
                padx=7,
                pady=7
            )

            am_inteles = ttk.Button(
                _about,
                text='Am inteles!',
                command=_about.destroy
            )

            am_inteles.pack(pady=7)

            _about.mainloop()

        about = tk.Menu(meniu, tearoff=0)
        about.add_command(label='About', command=about_gui)
        about.add_command(label='Exit', command=lambda: sys.exit(1))
        meniu.add_cascade(label='Help', menu=about)

        self.config(menu=meniu)

        title_label = ttk.Label(
            self,
            text='Credit card validator',
            font='Halvatica 11 bold italic',
            background='white'
        )

        title_label.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=5,
            pady=5
        )

        info_label = ttk.Label(
            self,
            text='Numar card:',
            font=11,
            background='white'
        )

        info_label.grid(
            row=2,
            column=0,
            sticky=tk.W,
            padx=5
        )

        card_entry = ttk.Entry(self, width=19)
        card_entry.grid(
            row=2,
            column=1,
            sticky=tk.W,
            padx=5
        )

        card_entry.focus()
        card_entry.bind('<Return>', lambda x: main(card_entry.get()))

        submit_button = ttk.Button(
            self,
            text='Submit',
            command=lambda: main(card_entry.get())
        )

        label_inutil_row3 = ttk.Label(self, text='')
        label_inutil_row3.grid(
            row=3,
            column=0
        )

        submit_button.grid(
            row=4,
            column=0,
            sticky=tk.SE
        )

        exit_button = ttk.Button(
            self,
            text='Exit',
            command=sys.exit
        )

        exit_button.grid(
            row=4,
            column=1,
        )

    def start(self):
        self.mainloop()


def main(card_number):

    """ Stabileste autenticitatea unui card de credit """

    import re
    import string

    alfabet = string.ascii_letters

    main_string = ''

    numar_card = card_number

    if numar_card == '':
        root = tk.Tk()
        root.withdraw()
        root.overrideredirect(1)
        messagebox.showwarning('Atentie', 'Intai adauga numarul cardului.')

    elif len(numar_card) != 19 and len(numar_card) != 16:
        root = tk.Tk()
        root.withdraw()
        root.overrideredirect(1)
        messagebox.showwarning('Atentie', 'Maxim 19 caractere cu tot cu spatiile libere.')

    for i in numar_card:
        if i not in alfabet:
            main_string += f'{i}'
        elif i in alfabet:
            root = tk.Tk()
            root.withdraw()
            root.overrideredirect(1)
            messagebox.showwarning('Atentie', 'Introduceti numai numere reale pozitive.')
            main_string = ''
            break

    lista_finala = re.findall(r'\S+', main_string)

    input_string = None

    try:
        input_string = lista_finala[0] + lista_finala[1] + lista_finala[2] + lista_finala[3]
    except IndexError:
        try:
            input_string = lista_finala[0]
        except IndexError:
            pass

    try:
        string_final = input_string[:15]

        lista_elm_patrate = [int(i)*2 for i in string_final[::2]]

        loop = 0

        while loop < 2:
            for cra in lista_elm_patrate:
                if len(str(cra)) == 2:
                    for n, i in enumerate(lista_elm_patrate):
                        if len(str(i)) == 2:
                            numar = str(i)
                            rezultat = int(numar[0]) + int(numar[1])
                            lista_elm_patrate[n] = rezultat
                            loop += 1

        lista_elem_simple = [int(z) for z in string_final[1::2]]

        lista_elem_simple.extend(lista_elm_patrate)

        total_lista = 0

        for i in lista_elem_simple:
            total_lista += i

        total = total_lista + int(input_string[15])

        if total % 10 == 0:
            root = tk.Tk()
            root.withdraw()
            root.overrideredirect(1)
            messagebox.showinfo('Coclusion', 'Numarul cardului introdus este valid.')
        else:
            root = tk.Tk()
            root.withdraw()
            root.overrideredirect(1)
            messagebox.showwarning('Conclusion', 'Numarul cardului introdus nu este valid.\nNu il folositi.')
    except (UnboundLocalError, TypeError):
        pass


if __name__ == '__main__':
    MyGui().start()
