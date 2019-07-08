def adunare(x, y):
    return x + y


def scadere(x, y):
    return x - y


def inmultire(x, y):
    return x * y


def impartire(x, y):
    return x / y


print("Select operation")
print("1.Adunare")
print('2.Scadere')
print('3.Inmultire')
print('4.Impartire')

choice = input("Enter choice(1/2/3/4):")

num1 = int(input('Enter your first number:'))
num2 = int(input('Ebter your second number:'))

if choice == '1':
    print(num1, '+', num2, '=', adunare(num1, num2))
elif choice == '2':
    print(num1, '-', num2, '=', scadere(num1, num2))
elif choice == '3':
    print(num1, '*', num2, '=', inmultire(num1, num2))
elif choice == '4':
    print(num1, '/', num2, '=', impartire(num1, num2))
else:
    print('Ai gresit numerele.')
