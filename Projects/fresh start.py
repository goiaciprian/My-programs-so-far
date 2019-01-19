
"""

Program care printeaza un numar introdus de utiliator de zecimale ale lui pi
Maxim 15 numere

"""


def pi_lenght():
    from math import pi
    from sys import exit
    mypi = str(pi)
    while True:
        user = input('Numar de zecimale\n::')
        if user == 'q':
            print('O zi buna')
            exit(1)
        try:
            user = int(user)
        except ValueError:
            print('Introdu numai numere intregi')
            continue
        if user > 15:
            print('Din motive de securitate am setat limita la 15 zecimale')
        else:
            print(f'Rezultatul este: {mypi[:user+2:]}')


if __name__ == "__main__":
    pi_lenght()
