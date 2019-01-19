import random
import math


class Razboinic:
    def __init__(self, nume=''):
        self.name = nume
        self.viata = 50
        self.atac = 20
        self.aparare = 10

    def atacul(self):
        valatac = self.atac * (random.random() + .5)

        return valatac

    def apararea(self):
        valaparere = self.aparare * (random.random() + .5)

        return valaparere


class Ninja:
    def __init__(self, nume=''):
        self.name = nume
        self.viata = 10
        self.atac = 20
        self.aparare = 50

    def atacul(self):
        valatac = self.atac * (random.random() + .5)

        return valatac

    def apararea(self):
        valaparere = self.aparare * (random.random() + .5)

        return valaparere


class Saman:

    def __init__(self, nume=''):
        self.name = nume
        self.viata = 20
        self.atac = 50
        self.aparere = 10

    def atacul(self):
        valatac = self.atac * (random.random() + .5)

        return valatac

    def apararea(self):
        valaparere = self.aparere * (random.random() + .5)

        return valaparere


class Battle:

    def incepelupta(self, razboinic1, razboinic2):

        while True:
            if self.rezultate(razboinic1, razboinic2) == 'Sfarsitul jocului.':
                print('Sfarsitul jocului.')
                break

            if self.rezultate(razboinic2, razboinic1) == 'Sfarsitul jocului.':
                print('Sfarsitul jocului.')
                break

    @staticmethod

    def rezultate(razboinicA, razboinicB):

        razvalatac = razboinicA.atacul()

        razvalaparare = razboinicB.apararea()

        daunerazB = math.ceil(razvalatac - razvalaparare)

        razboinicB.viata = razboinicB.viata - daunerazB

        print('{} l-a atacat pe {},daune {}.'.format(razboinicA.name, razboinicB.name, daunerazB))

        print('{} are {} viata.'.format(razboinicB.name, razboinicB.viata))

        if razboinicB.viata <= 0:
            print('{} a murit, {} a castigat.'.format(razboinicB.name, razboinicA.name))
            return 'Sfarsitul jocului.'
        else:
            return None


def main():

    print("""Alege:\n
Razboinic - 1\nNinja - 2\nSaman - 3\n""")
    clasa = input('Alege-ti clasa:')
    if clasa == '1':
        nume = str(input('Introdu numele razboinicului:'))
        utilizator = Razboinic(nume)
        print('Ai ales razboinic.')
        calculator = random.randint(1, 3)
        if calculator == 1:
            calculator = Razboinic('Calculator')
            print('Calculatorul a ales razboinic.')
        elif calculator == 2:
            calculator = Ninja('Calculator')
            print('Calculatorul a ales ninja.')
        else:
            calculator = Saman('Calculator')
            print('Calculatorul a ales saman.')

        batalie = Battle()
        batalie.incepelupta(utilizator, calculator)
    elif clasa == '2':
        nume = str(input('Introdu numele razboinicului:'))
        utilizator = Ninja(nume)
        print('Ai ales ninja.')
        calculator = random.randint(1, 3)
        if calculator == 1:
            calculator = Razboinic('Calculator')
            print('Calculatorul a ales razboinic.')
        elif calculator == 2:
            calculator = Ninja('Calculator')
            print('Calculatorul a ales ninja.')
        else:
            calculator = Saman('Calculator')
            print('Calculatorul a ales saman.')

        batalie = Battle()
        batalie.incepelupta(utilizator, calculator)
    elif clasa == '3':
        nume = str(input('Introdu numele razboinicului:'))
        utilizator = Saman(nume)
        print('Ai ales saman.')
        calculator = random.randint(1, 3)
        if calculator == 1:
            calculator = Razboinic('Calculator')
            print('Calculatorul a ales razboinic.')
        elif calculator == 2:
            calculator = Ninja('Calculator')
            print('Calculatorul a ales ninja.')
        else:
            calculator = Saman('Calculator')
            print('Calculatorul a ales saman.')

        batalie = Battle()
        batalie.incepelupta(utilizator, calculator)
    else:
        print('Trebuie un numar de la 1 la 3.')
        return main()

    restart = input('Mai joci?')
    if not restart.isdecimal() and restart == 'da' or restart == 'Da':
        main()
    else:
        quit()


main()
