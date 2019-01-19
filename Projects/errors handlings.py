# try:
#     for i in ['a', 'b', 'c']:
#         print(i**2)
# except TypeError:
#     print('aia e')

# try:
#     x = 5
#     y = 0
#
#     z = x/y
# except ZeroDivisionError:
#     z = 0
#     print('0')
# finally:
#     print('All done')


def ask():
    while True:
        try:
            numar = input('Numarul: ')
            print(int(numar)**2)
        except ValueError:
            print('Introdu un numar')


ask()
