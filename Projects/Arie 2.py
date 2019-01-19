"""Asta este un calculator pentru aria cercului si a triunghiului"""

print('Se porneste..')

nume = input('Nume: ')

def start():
    option = input('Scrie c pentru aria cercului sau t pentru aria triunghiului:')

    if option == 'c' or option == 'C' and option.isalpha():
        raza = input('Cat este raza:')
        if raza.isdecimal():
            aria = 3.14159 * float(raza) ** 2
            print('Aria este :', aria)
        else:
            print('prajit')
    elif option == 't' or option == 'T' and option.isalpha():
        baza = input('Cat este baza:')
        inaltimea = input('Cat este inlatimea:')
        if baza.isdecimal() and inaltimea.isdecimal():
            aria = 0.5 * float(baza) * float(inaltimea)
            print('Aria este :', aria)
        else:
            print('prajit')
    else:
        print('Esti bulangiu te-am rugat sa bagi numai c sau t...')

    restart = input('Vrei sa incerci iar?')
    if restart == 'da':
        start()
    else:
        quit()
start()
