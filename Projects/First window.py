from tkinter import *
from tkinter import messagebox

def main(event):
    choice = egalEntry.get()
    if choice == '1':
        root.destroy()

        def mama(event):
            adunare.destroy()
            centru(event)

        def sum(event):
            num1 = int(a.get())
            num2 = int(b.get())

            sum = num1 + num2

            sumEntry.delete(0, 'end')

            sumEntry.insert(0, sum)

        adunare = Tk()

        adunare.title('Adunare')
        adunare.geometry("250x175")

        Label(adunare, text='Introdu numerele pentru adunare:       \n').grid(row=0, column=2, sticky=W)
        Label(adunare, text='Introdu primul numar: ').grid(row=1, column=2, sticky=W)
        Label(adunare, text='Introdu al doilea numar: ').grid(row=3, column=2, sticky=W)
        Label(adunare, text='Rezultatul este: ' ).grid(row=5, column=2, sticky=W)

        a = Entry(adunare)
        a.grid(row=2, column=2, sticky=W)

        b = Entry(adunare)
        b.grid(row=4, column=2, sticky=W)

        sumEntry = Entry(adunare)
        sumEntry.grid(row=6, column=2, sticky=W)

        egal = Button(adunare, text='Egal',)
        egal.bind('<Button-1>', sum)
        egal.grid(row=5, column=2, sticky=E)

        reButton = Button(adunare, text='Inapoi')
        reButton.bind('<Button-1>', mama)
        reButton.grid(row=6, column=2, sticky=E)

        adunare.mainloop()

    elif choice == '2':
        root.destroy()

        def mama(event):
            adunare.destroy()
            centru(event)

        def sum(event):
            num1 = int(a.get())
            num2 = int(b.get())

            sum = num1 - num2

            sumEntry.delete(0, 'end')

            sumEntry.insert(0, sum)

        adunare = Tk()

        adunare.title('Scadere')
        adunare.geometry("250x175")

        Label(adunare, text='Introdu numerele pentru scadere:       \n').grid(row=0, column=2, sticky=W)
        Label(adunare, text='Introdu primul numar: ').grid(row=1, column=2, sticky=W)
        Label(adunare, text='Introdu al doilea numar: ').grid(row=3, column=2, sticky=W)
        Label(adunare, text='Rezultatul este: ' ).grid(row=5, column=2, sticky=W)

        a = Entry(adunare)
        a.grid(row=2, column=2, sticky=W)

        b = Entry(adunare)
        b.grid(row=4, column=2, sticky=W)

        sumEntry = Entry(adunare)
        sumEntry.grid(row=6, column=2, sticky=W)

        egal = Button(adunare, text='Egal',)
        egal.bind('<Button-1>', sum)
        egal.grid(row=5, column=2, sticky=E)

        reButton = Button(adunare, text='centru')
        reButton.bind('<Button-1>', mama)
        reButton.grid(row=6, column=2, sticky=E)

        adunare.mainloop()

    elif choice == '3':
        root.destroy()

        def mama(event):
            adunare.destroy()
            centru(event)

        def sum(event):
            num1 = int(a.get())
            num2 = int(b.get())

            sum = num1 * num2

            sumEntry.delete(0, 'end')

            sumEntry.insert(0, sum)

        adunare = Tk()

        adunare.title('Inmultire')
        adunare.geometry("250x175")

        Label(adunare, text='Introdu numerele pentru inmultire:       \n').grid(row=0, column=2, sticky=W)
        Label(adunare, text='Introdu primul numar: ').grid(row=1, column=2, sticky=W)
        Label(adunare, text='Introdu al doilea numar: ').grid(row=3, column=2, sticky=W)
        Label(adunare, text='Rezultatul este: ' ).grid(row=5, column=2, sticky=W)

        a = Entry(adunare)
        a.grid(row=2, column=2, sticky=W)

        b = Entry(adunare)
        b.grid(row=4, column=2, sticky=W)

        sumEntry = Entry(adunare)
        sumEntry.grid(row=6, column=2, sticky=W)

        egal = Button(adunare, text='Egal',)
        egal.bind('<Button-1>', sum)
        egal.grid(row=5, column=2, sticky=E)

        reButton = Button(adunare, text='Inapoi')
        reButton.bind('<Button-1>', mama)
        reButton.grid(row=6, column=2, sticky=E)

        adunare.mainloop()

    elif choice == '4':
        root.destroy()

        def mama(event):
            adunare.destroy()
            centru(event)

        def sum(event):
            num1 = int(a.get())
            num2 = int(b.get())

            sum = num1 / num2

            sumEntry.delete(0, 'end')

            sumEntry.insert(0, sum)

        adunare = Tk()

        adunare.title('Impartire')
        adunare.geometry("250x175")

        Label(adunare, text='Introdu numerele pentru impartire:       \n').grid(row=0, column=2, sticky=W)
        Label(adunare, text='Introdu primul numar: ').grid(row=1, column=2, sticky=W)
        Label(adunare, text='Introdu al doilea numar: ').grid(row=3, column=2, sticky=W)
        Label(adunare, text='Rezultatul este: ' ).grid(row=5, column=2, sticky=W)

        a = Entry(adunare)
        a.grid(row=2, column=2, sticky=W)

        b = Entry(adunare)
        b.grid(row=4, column=2, sticky=W)

        sumEntry = Entry(adunare)
        sumEntry.grid(row=6, column=2, sticky=W)

        egal = Button(adunare, text='Egal',)
        egal.bind('<Button-1>', sum)
        egal.grid(row=5, column=2, sticky=E)

        reButton = Button(adunare, text='Inapoi')
        reButton.bind('<Button-1>', mama)
        reButton.grid(row=6, column=2, sticky=E)

        adunare.mainloop()

    else:

        def mama(evet):
            els.destroy()

        messagebox.showwarning('Eroare','Trebuie sa introduceti unul dintre numerelde de mai sus.')

def inchide(event):
    root.destroy()

def centru(event):

    def inchide(event):
        root.destroy()

    root = Tk()

    root.title('Calculator')
    Label(root, text='Introdu numarul corespunzator:         ').grid(row=0, column=2, sticky=W)
    Label(root, text='1.Adunare').grid(row=1, column=2, sticky=W)
    Label(root, text='2.Scadere').grid(row=2, column=2, sticky=W)
    Label(root, text='3.Inmultrire').grid(row=3, column=2, sticky=W)
    Label(root, text='4.Impartire').grid(row=4, column=2, sticky=W)

    egalEntry = Entry(root)
    egalEntry.grid(row=5, column=2)

    eButton = Button(root, text='Submit')
    eButton.bind('<Button-1>', main)
    eButton.grid(row=6, column=2)

    qButton = Button(root, text='Quit')
    qButton.bind('<Button-1>', inchide)
    qButton.grid(row=6, column=3)

    root.mainloop()

root = Tk()

root.title('Calculator')
Label(root, text='Introdu numarul corespunzator:         ').grid(row=0, column=2, sticky=W)
Label(root, text='1.Adunare').grid(row=1, column=2, sticky=W)
Label(root, text='2.Scadere').grid(row=2, column=2, sticky=W)
Label(root, text='3.Inmultrire').grid(row=3, column=2, sticky=W)
Label(root, text='4.Impartire').grid(row=4, column=2, sticky=W)

egalEntry = Entry(root)
egalEntry.grid(row=5, column=2)

eButton = Button(root, text='Submit')
eButton.bind('<Button-1>', main)
eButton.grid(row=6, column=2)

qButton = Button(root, text='Quit')
qButton.bind('<Button-1>', inchide)
qButton.grid(row=6, column=3)


root.mainloop()