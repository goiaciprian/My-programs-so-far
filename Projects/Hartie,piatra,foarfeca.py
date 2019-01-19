from random import randint

def main():
    player = input('hartie(h), piatra(p), foarfeca(f) ?:')
    chosen = randint(1, 3)

    if  chosen == 1:
        print('Calculatorul a ales piatra.')
    elif chosen == 2:
        print('Calculatorul a ales hartie.')
    else:
        print('Calculatorul a ales foarfeca.')

    if player == "h":
        aleg = 'hartie'
    elif player == 'p':
        aleg = 'piatra'
    elif player == 'f':
        aleg = 'foarfeca'

    print(aleg, 'vs', end=' ')


    p = "piatra"
    h = 'hartie'
    f = 'foarfeca'

    if  chosen == 1:
        computer = p
    elif chosen == 2:
        computer = h
    else:
        computer = f

    print(computer)

    if aleg == computer:
        print('Egal!')
    elif aleg == p and computer == f:
        print('Ai castigat!')
    elif aleg == p and computer == h:
        print('Ai pierdut!')
    elif aleg == h and computer == p:
        print('Ai castigat!')
    elif aleg == h and computer == f:
        print('Ai pierdut!')
    elif aleg == f and computer == p:
        print('Ai gastigat!')
    else:
        print('Ai pierdut!')

    restart = input('Mai joci?')
    if restart == 'da' and restart.isalpha():
        main()
    else:
        quit()
main()
