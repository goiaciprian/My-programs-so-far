#!/usr/bin/env python

from tkinter import *
from tkinter import ttk, messagebox, TclError
from time import sleep
from win10toast import ToastNotifier
import sys
import os


def resource_path(relative_path):
    """ Stabileste path-ul catre un folder temporar unde sunt incluse datele pt pyinstaller , daca este cazul """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


image_path = resource_path("clockicon.ico")


class MainApp(Tk):  # Obiect tip GUI tkitner

    def __init__(self):
        Tk.__init__(self)

        self.title('Alarma')

        self.resizable(False, False)

        self.eval(f"tk::PlaceWindow {self.winfo_toplevel()} center")

        try:
            self.iconbitmap(image_path)
        except TclError:
            pass

        self.configure(
            background='white'
        )

        titlu_label = ttk.Label(
            self,
            text='Cronometru cu alarma',
            font='Halvatica 10 bold',
            background='white'
        )

        titlu_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        primul_label = ttk.Label(
            self,
            text='Minute:',
            font='Halvatica 9 bold',
            background='white'
        )

        primul_label.grid(
            row=1,
            column=0,
            sticky=W,
        )

        user_entry = ttk.Entry(
            self,
            justify=RIGHT,
            width=10
        )

        user_entry.focus()

        user_entry.bind('<Return>', lambda user_entry_get: main_app(user_entry.get()))

        user_entry.grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        help_button = ttk.Button(
            self,
            text='Help',
            command=lambda: messagebox.showinfo(
                'Help',
                'Programul este compatibil doar cu windows 10.\n'
                'Introduceti un numar intreg pozitiv in casuta.\n'
                'Folositi 0 ca sa testati alarma.'
            ),
            width=5
        )

        help_button.grid(
            row=1,
            column=0,
            sticky=E
        )

        def main_app(user_get):  # Aplicatia in sine
            self.destroy()
            import sys
            notificare = ToastNotifier()  # Clasa pt notificari

            input_user = user_get  # Folosim 0 daca utilizatorul nu introduce nimic
            if input_user == '' or input_user == ' ':
                input_user = 0

            try:  # Verificat input-ul sa fie un numar intreg pozitiv
                minutes = int(input_user)
            except ValueError:
                root = Tk()
                root.overrideredirect(1)
                root.withdraw()
                messagebox.showerror(
                    'Eroare',
                    f'Trebuie sa introduceti un numar intreg pozitiv, nu {input_user}.'
                )
                sys.exit(1)

            if minutes < 0:
                root = Tk()
                root.overrideredirect(1)
                root.withdraw()
                messagebox.showerror(
                    'Eroare',
                    'Numarul trebuie sa fie real pozitiv.'
                )

                sys.exit(1)

            seconds = minutes * 60  # Trnsformam minutele in secunde pt fucntia sleep

            if minutes == 1:  # Facem acordul gramatical in functie de input
                unit_word = " minut"
            else:
                unit_word = " minute"

            try:  # Facem diferenta dintre
                if minutes > 0:
                    notificare.show_toast(
                        'Alarma',
                        f"Alarma se va declansa dupa {str(minutes)}{unit_word}.",
                        icon_path=image_path,
                        duration=6,
                        threaded=False
                    )
                    sleep(seconds)
                for i in range(3):
                    print(chr(7))
                    sleep(1)
                notificare.show_toast(
                    'Alarma',
                    "Timpul a expirat.",
                    icon_path=image_path,
                    duration=6,
                    threaded=False
                )
            except KeyboardInterrupt:
                notificare.show_toast(
                    'Alarma',
                    "Intrerupt de utilizator.",
                    icon_path=image_path,
                    duration=6,
                    threaded=True
                )
                sys.exit(1)

        submit_button = ttk.Button(
            self,
            text='Submit',
            command=lambda: main_app(user_entry.get()),
            width=10
        )

        submit_button.grid(
            row=2,
            column=0,
            columnspan=1,
            padx=5,
            pady=5,
            sticky=W
        )

        exit_button = ttk.Button(
            self,
            text='Exit',
            command=lambda: sys.exit(1)
        )

        exit_button.grid(
            row=2,
            column=0,
            columnspan=1,
            sticky=E,
            padx=5,
            pady=5
        )

    def start(self):
        self.mainloop()


if __name__ == '__main__':
    MainApp().start()
