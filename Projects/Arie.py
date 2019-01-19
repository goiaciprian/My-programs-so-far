
"""Asta este un calculator pentru aria cercului si a triunghiului"""

print('Se porneste..')

nume = input('Nume: ')

d = []
history = {str(nume): d}

while True:
    option = input('Scrie c pentru cerc sau t pentru triunghi:').lower()

    if option == 'c' and option.isalpha():
        raza = float(input('Cat este raza:'))
        aria = 3.14159 * raza ** 2
        print('Aria este %.02f' % aria)
        d.append(aria)
        if input('Mai bagi?').lower() == 'da':
            continue
        else:
            break
    elif option == 't' and option.isalpha():
        baza = float(input('Cat este baza:'))
        inaltimea = float(input('Cat este inlatimea:'))
        aria2 = 0.5 * baza * inaltimea
        print('Aria este %.02f' % aria2)
        d.append(aria2)
        if input('Mai bagi?').lower() == 'da':
            continue
        else:
            break
    else:
        print('Esti bulangiu te-am rugat sa bagi numai c sau t...')
print(history)
with open('C:\\Users\camio\\Desktop\\istoric.txt', mode='w') as istoric:
    istoric.write(str(history))
