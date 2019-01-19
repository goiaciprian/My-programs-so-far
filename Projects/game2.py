import random


class pistol:

    def __init__(self, name = '', daune = 1, aparare = 1):
        self.name = name
        self.daune = daune
        self.viata = 100
        self.aparare = aparare

    def atacul(self):
        valatac = self.daune * random.randint(1, 25)
        return valatac

    def apararea(self):
        valaparare = self.aparare * random.randint(1, 20)
        return valaparare

class m4(object):

    def __init__(self, name = '', daune = 1, aparare = 1):
        self.name = name
        self.daune = daune
        self.viata = 100
        self.aparare = aparare

    def atacul(self):

        valatac = self.daune * random.randint(1, 75)

        return valatac

    def apararea(self):

        valaparare = self.aparare * random.randint(1, 20)
        return valaparare


class battle:

    def incepelupta(self, luptator1, luptator2):

         while True:

             if self.rezultate(luptator1, luptator2) == 'Sfarsitul jocului.':

                 print('Sfarsitul jocului.')

                 break

             if self.rezultate(luptator2, luptator1) == 'Sfarsitul jocului.':
                 print('Sfarsitul jocului.')
                 break

    @staticmethod

    def rezultate(luptatora, luptatorb):

        razvalatac = int(luptatora.atacul())

        razvalaparare = luptatora.apararea()

        dauneb = razvalatac - razvalaparare

        luptatorb.viata = luptatorb.viata - dauneb

        print('{} l-a atacat pe {},daune {}.'.format(luptatora.name, luptatorb.name, dauneb))

        print('{} are {} viata.'.format(luptatorb.name, luptatorb.viata))

        if luptatorb.viata <= 0:

            print('{} a murit, {} a castigat.'.format(luptatorb.name, luptatora.name))

            return 'Sfarsitul jocului.'

        else:
            return None


def main():
    nume = str(input('Introdu numele aici:'))
    print("""Alege arma\n1-pentru pistol\n2-pentru m4""")
    arma = str(input('Alege-ti arma:'))

    if arma == '1':
        utilizator = pistol(nume)
        pick = random.randint(1,2)
        print('Ai ales pistol.')
        if pick == 1:
            calculator = pistol('Calculator')
            print('Calculatorul a ales pistol.')
        else:
            calculator = m4('Calculator')
            print('Calculatorul a ales m4.')

        bataie = battle()
        bataie.incepelupta(utilizator, calculator)

    elif arma == '2':
        utilizator = m4(nume)
        pick = random.randint(1, 2)
        print('Ai ales m4.')
        if pick == 1:
            calculator = pistol('Calculator')
            print('Calculatorul a ales pistol.')
        else:
            calculator = m4('Calculator')
            print('Calculatorul a ales m4.')

        bataie = battle()
        bataie.incepelupta(utilizator, calculator)

    else:
        print('Trebuie sa alegi o arma.')
        main()

    restart = input('Mai joci?')
    if restart == 'da' or restart == 'Da':
        main()
    else:
        quit()


main()
