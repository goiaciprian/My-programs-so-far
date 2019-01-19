"""

Program care generaza un numar,dat de utilizator, de zeimale ale lui e

"""


def e_lenght():
    from math import e
    from sys import exit
    mye = str(e)
    while True:
        user = input('Introdu numarul de zecimale\n::')
        if user == 'q':
            print('O zi buna')
            exit(1)
        else:
            try:
                user = int(user)
            except ValueError:
                print('Introduceti numai numere intregi pozitive')
                continue
            if user > 15:
                print('Din motive de sigurant am setat limita de zecimale la 15')

            print(f'Rezultatul este: {mye[:user+2:]}')


if __name__ == '__main__':
    e_lenght()