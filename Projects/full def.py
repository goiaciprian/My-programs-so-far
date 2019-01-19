import os

path = os.path.expanduser('~/Desktop/File.txt')


def inceput():
    global nume
    global parola
    print("""Bun venit!
Alge una dintre urmatoarele optiuni:
1 - Logare(l sau 1)
2 - Inregistrare(i sau 2)""")
    while True:
        alegere = input('::')
        nume = input('Nume: ')
        parola = input('Parola: ')
        if alegere.lower() == 'l' or alegere == '1':
            login()
        elif alegere.lower() == 'i' or alegere == '2':
            singup()
        else:
            print('Alege una dintre variante (l sau i).')
            continue


def login():
    with open(path, 'r') as fle:
        content = fle.read()
        if ' ' + nume + ' ' + parola in content:
            print('Slabut')
        else:
            print('Ai gresit contul baiatul meu')
            inceput()


def singup():
    with open(path, 'a') as fil:
        fil.write(' ' + nume + ' ' + parola)
        print('Te-ai inregistrat cu succes.')
        inceput()


if __name__ == '__main__':
    if os.path.isfile(path):
        inceput()
    else:
        with open(path, 'a') as file:
            file.write('ceva')
            inceput()
