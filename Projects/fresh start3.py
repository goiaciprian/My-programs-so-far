"""

Fibonacci sequence

"""


def fibonacci_sequence(nterms=1):
    f1, f2 = 0, 1
    count = 0
    if nterms <= 0:
        print('Introdu un numar real pozitiv')
    elif nterms == 1:
        print(f"Numerele pana la {nterms}:")
        print(f1)
    else:
        print(f"Numerele pana la {nterms}:")
        while count < nterms:
            print(f1, end=', ')
            fth = f1 + f2
            f1 = f2
            f2 = fth
            count += 1


if __name__ == '__main__':
    while True:
        user = input('\nNumarul de termeni\n:')
        if user == 'q':
            print('O zi buna')
            exit(1)
        try:
            user = int(user)
        except ValueError:
            print('Introdu numai numere reale pozitive')
        finally:
            fibonacci_sequence(user)
