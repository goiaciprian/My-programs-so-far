#!user/bin/env python

"""Program care gaseste ip-ul public, privat si face localizare geografica in functie de cel public"""

# Importam modulele necesare
from urllib.request import urlopen
from urllib.error import URLError
import socket
import json
from tkinter import *
from tkinter import ttk, messagebox
import sys

# Gasim Ip-ul local si public
try:
    local_ip = socket.gethostbyname(socket.gethostname())
    public_ip = urlopen('http://api.ipify.org').read().decode('utf8')  # Site special pt aflarea ip-ului public
except URLError:
    root = Tk()
    root.overrideredirect(1)
    root.withdraw()
    messagebox.showerror('Connection error!', 'Ai nevoie de conexiune la internet.')
else:

    # Localizare geografica
    geo_key_ipstack = 'ddc0c2da33152ee9a66b63615c601d42'  # Cheie pt acces baza de date online

    # Copiem datele necesare din baza de date
    answer = urlopen(f'http://api.ipstack.com/{public_ip}?access_key={geo_key_ipstack}').read().decode('utf8')

    # Transformam string-ul din baza de date in dinctionar
    geolocalizare = json.loads(answer)

    # Creem un GUI pt utilizator
    root = Tk()

    root.title('Client Localizare')

    root.resizable(False, False)

    root.configure(background='white')

    try:
        root.iconbitmap(r'C:\Users\camio\PycharmProjects\Proiecte\iconita.ico')
    except TclError:
        pass

    titlu = Label(root, text='Informatii:', font='Helvetica 18 bold', background='white').grid(row=0, column=0,
                                                                                               columnspan=1, padx=5,
                                                                                               pady=5)

    privat_label = Label(root, text='Ip privat: {}'.format(local_ip), background='white', font=20).grid(row=1, column=0,
                                                                                                        padx=5,
                                                                                                        sticky=W)
    public_label = Label(root, text='Ip public: {}'.format(public_ip), font=20, background='white').grid(row=2,
                                                                                                         column=0,
                                                                                                         padx=5,
                                                                                                         sticky=W)
    tip_label = Label(root, text='Tip ip: {}'.format(geolocalizare['type']), font=20, background='white').grid(row=3,
                                                                                                               column=0,
                                                                                                               padx=5,
                                                                                                               sticky=W)
    continent_label = Label(root, text='Continent: {} - {}'.format(geolocalizare['continent_name'],
                                                                   geolocalizare['continent_code']),
                            font=20, background='white').grid(row=4, column=0, padx=5, sticky=W)
    tara_label = Label(root, text='Tara: {} - {}'.format(geolocalizare['country_name'], geolocalizare['country_code']),
                       font=20, background='white').grid(row=5, column=0, padx=5, sticky=W)
    regiune_label = Label(root, text='Regiune: {} - {}'.format(geolocalizare['region_name'],
                                                               geolocalizare['region_code']), font=20,
                          background='white').grid(row=6, column=0, padx=5, sticky=W)
    oras_label = Label(root, text='Oras: {}'.format(geolocalizare['city']), font=20, background='white').grid(row=7,
                                                                                                              column=0,
                                                                                                              padx=5,
                                                                                                              sticky=W)
    cod_postal_label = Label(root, text='Cod Postal: {}'.format(geolocalizare['zip']), font=20, background='white').\
        grid(row=8, column=0, padx=5, sticky=W)

    close_button = ttk.Button(root, text='Iesire', command=lambda: sys.exit()).grid(row=10, column=0, columnspan=1,
                                                                                    padx=5, pady=5)

    root.mainloop()
