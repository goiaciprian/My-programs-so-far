from tkinter import *
from tkinter import ttk
import os

creds = 'tempfile.temp'


def singup():
    global pwordE
    global nameE
    global roots

    roots = Tk()
    roots.title('Signup')
    intruction = Label(roots, text='Please Enter new Credidentials\n')
    intruction.grid(row=0, column=0, sticky=E)

    nameL = Label(roots, text='New Username: ')
    pwordL = Label(roots, text='New Password: ')
    nameL.grid(row=1, column=0,
               sticky=W)
    pwordL.grid(row=2, column=0, sticky=W)

    nameE = Entry(roots)
    pwordE = Entry(roots,
                   show='*')
    nameE.grid(row=1, column=1)
    pwordE.grid(row=2, column=1)

    signupButton = Button(roots, text='Signup', command=FSSingup)
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()


def FSSingup():

    with open(creds, 'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.write('\n')
        f.close()

    roots.destroy()

    Login()


def Login():

    global nameEL
    global pwordEL
    global rootA

    rootA = Tk()
    rootA.title('Log in')

    intruction = Label(rootA, text='Please login')
    intruction.grid(stick=E)

    nameL = Label(rootA, text='Username: ')
    pwordL = Label(rootA, text='Password: ')
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)

    nameEL = ttk.Entry(rootA)
    pwordEL = ttk.Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)

    login_button = ttk.Button(rootA, text='Login', command=CheckLogin)
    login_button.grid()

    rmuser = ttk.Button(rootA, text='Delete user', command=DelUser)
    rmuser.grid()

    rootA.mainloop()


def CheckLogin():

    with open(creds) as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()

    if nameEL.get() == uname and pwordEL.get() == pword:
        r = Tk()
        r.title(':D')
        r.geometry('150x150')
        rlbl = Label(r, text='\n[+] Logged In')
        rlbl.pack()
        r.mainloop()

    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x150')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()


def DelUser():
    os.remove(creds)
    rootA.destroy()
    singup()


if os.path.isfile(creds):
    Login()
else:
    singup()
