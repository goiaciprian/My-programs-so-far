"""

Prime numbers

"""


def prime_numbers(inrange):
    return [k for k in range(1, inrange) if k / 1 == k and k / k == 1]


if __name__ == '__main__':
    while True:
        user = input('::')
        if user == 'q':
            exit(1)
        try:
            user = int(user)
        except ValueError:
            print('Introduceti numai numere reale poitive')
            continue
        for i in prime_numbers(user+1):
            print(i, end=', ')
