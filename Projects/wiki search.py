#!usr/bin/env python

# Api wiki : https://en.wikipedia.org/w/api.php?action=opensearch&search=

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


def resource_path(relative_path):
    import sys
    import os
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class TkWindow(tk.Tk):

    @staticmethod
    def checkwiki(entry_get=' ', limba='ro'):

        from urllib.request import urlopen
        from json import loads
        from re import split

        userinp = entry_get
        user = userinp.split()
        search = ''
        for i in user:
            search = search + '_' + i

        wikiurl = f'https://{limba}.wikipedia.org/w/api.php?action=opensearch&format=json&search={search[1::]}'
        urldata = urlopen(wikiurl).read().decode('utf-8')
        data = loads(urldata)
        return_list = [f'{page}: {link}' for page, link in zip(data[1], data[3])]
        for element in enumerate(return_list):
            return_list[element[0]] = element

        extended_return_list = []

        for tupl in return_list:
            for _ in tupl[1]:
                rezultat = split(':', tupl[1])
                extended_return_list.append(rezultat)  # adauga acelasi item de trei ori (glitch)
        print(return_list)
        print(extended_return_list)

    def __init__(self):
        tk.Tk.__init__(self)

        self.title('Search Wiki')
        self.config(background='white')
        self.geometry('%dx%d+%d+%d' % (840, 420, 220, 150))
        self.resizable(False, False)

        self.serch_frame = tk.Frame(self, background='white')
        self.serch_frame.pack(fill=tk.BOTH, expand=1)

        # Stackoverflow example --> not working as expected (scratch16)
        self.display_frame = tk.Frame(self, bg='white')
        self.display_frame.pack(fill=tk.BOTH, expand=1)

        self.canvas_frame = tk.Canvas(self.display_frame, bg='white')
        self.canvas_frame.pack(side='left', fill=tk.BOTH, expand=True)

        self.inside_frame = tk.Frame(self.canvas_frame, background='white')
        self.inside_frame.pack(fill=tk.BOTH, expand=True)

        self.vs = tk.Scrollbar(self, orient="vertical", command=self.canvas_frame.yview)
        self.canvas_frame.configure(yscrollcommand=self.vs.set)
        self.canvas_frame.create_window((4, 4), window=self.inside_frame, anchor="nw", tags="self.frame")
        self.vs.pack(side="right", fill="y")

        def try_or_pass():
            try:
                self.checkwiki(search_entry.get())
            except (Exception, TypeError) as e:
                print(e)
            # for n in enumerate(self.checkwiki(search_entry.get())):
            #     display_label = tk.Label(self.canvas_frame, bg='white')
            #     display_label['text'] = n[1] + '\n'
            #     display_label.pack()

        # Search frame widgets
        free_space = tk.Label(
            self.serch_frame,
            background='white',
            text=' '*70
        )
        free_space.grid(
            row=1,
            column=1
        )

        img = ImageTk.PhotoImage(Image.open(resource_path('images/32px.jpeg')))

        img_label = tk.Label(
            self.serch_frame,
            image=img,
            background='white'
        )
        img_label.image = img
        img_label.grid(
            row=1,
            column=2,
            padx=10
        )

        label = ttk.Label(
            self.serch_frame,
            background='white',
            text='Search Wiki:',
            font='Times 14'
        )
        label.grid(
            row=1,
            column=3,
            pady=10,
            sticky=tk.W
        )

        search_entry = ttk.Entry(
            self.serch_frame,
        )

        search_entry.bind(
            '<Return>',
            try_or_pass
        )
        search_entry.grid(
            row=1,
            column=4,
            padx=10,
            sticky=tk.W
        )
        submit_button = ttk.Button(
            self.serch_frame,
            text='Search',
            command=try_or_pass
        )
        submit_button.grid(
            row=1,
            column=5
        )

    def start(self):
        self.mainloop()


if __name__ == '__main__':
    TkWindow().start()
