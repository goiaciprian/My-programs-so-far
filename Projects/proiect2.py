

""""
Gasestea cea mai simpla varianta a unei matrice in functie de 0 si 1
0 - fundalul imaginii
1 - obiect in prim-plan
"""


def main():

    """" Aplicatia principala """

    main_list = []  # creeaza o lista pentru toate rndurile din matrice

    while True:  # Creeaza un loop pana se introduce numarul de randuri si coloane
        try:  # Verifica codul de erori
            main_input = input('::')  # se introduce nr de randuri si coloane
            if len(main_input) > 3:
                print('Lungimea maxima este 3.')
                continue
            elif main_input[0] == '0' or main_input[2] == '0':
                print('Nu poti introduce 0.')
                continue
            randuri = int(main_input[0])  # numarul devine integer
            coloane = int(main_input[2])  # ^^^

        except (IndexError, ValueError):  # Executa codul de mai jos daca nu sunt gasite erorile specificate
            print('Din nou')

        else:  # Executa restul codului
            i = 0  # variabila pentru oprirea while loop-ului

            while i <= (randuri - 1):  # incepe loop-ul in functie de nr de randuri
                matrice = input('::')  # de introduce modelul de matrice
                if matrice.__len__() == ((coloane * 2) - 1):  # se compara lungimea cu nr coloanelor
                    i += 1  # crestem i ca sa oprim while loop-ul
                    main_list.append(list(matrice))  # adauga o lista cu elemnte in lista principala
                else:  # daca nu se indeplineste prima conditie se printeaza Lungime depasita
                    print('Lungimea nu corespunde.')  # ^^^

            lista_fara_spatii = []

            for rand in main_list:  # ia fiecare rand in parte
                for spatiu in rand:  # loop special pentru spatii
                    if spatiu == ' ':  # verificam daca exista un spatiu in lista
                        rand.remove(' ')  # stergem spatiile
                lista_fara_spatii.append(rand)  # adaugam numerele in lista

            # In caz ca se introduce un singur 1
            count = 0

            for rand in lista_fara_spatii:
                if '1' in rand:
                    count += 1
            if count == 1:
                print('[1]')
            else:

                # Gaseste primul 1
                for rand in lista_fara_spatii:  # ia fiecare rand din lista
                    if '1' in rand:  # verifica daca exista 1 in rand
                        break
                    else:
                        rand.clear()  # sterge randul care este fara 1

                # Gaseste ultimul 1
                for rand in reversed(lista_fara_spatii):  # ia fiecare rand din lista , de la sfarsit
                    if '1' in rand:  # verifica daca exista 1 in lista
                        break
                    else:
                        rand.clear()  # sterge randul care este fara 1

                # Stergem listele goale

                for lista_goala in lista_fara_spatii:  # Sterge primele []
                    if not lista_goala:
                        lista_fara_spatii.remove([])  # Comanda remove nu sterge toate []

                for lista_goala in reversed(lista_fara_spatii):  # Sterge ultimele []
                    if not lista_goala:
                        lista_fara_spatii.remove([])

                # Gaseste primul 1 din dreapta
                lista_dreapta = []  # lista cu elementele din coloana din dreapta

                for rand in lista_fara_spatii:  # adauga elemntele din coloana din stanga
                    lista_dreapta.append(rand[coloane - 1])

                if '1' in lista_dreapta:  # verifica daca este 1 in lista
                    pass
                else:
                    for rand in lista_fara_spatii:  # sterge coloana formata din 0
                        rand.pop(coloane - 1)

                # Gaseste primul 1 din stanga
                lista_stanga = []  # lista provizorie cu elementele din stanga

                for rand in lista_fara_spatii:  # adauga in lista_stanga elementele din coloana din stanga
                    lista_stanga.append(rand[0])

                if '1' in lista_stanga:  # verifica daca 1 e in lista
                    pass  # nu face nimic
                else:
                    for rand in lista_fara_spatii:  # daca nu e 1 in losta stergem coloana de 0
                        rand.pop(0)

                # Printeaza lista sib forma de matrice
                for rand in lista_fara_spatii:
                    print(rand)

            raspuns = input('Iesire?(d sau n):')  # Intreaba user-ul daca vrea sa inchida programul
            if raspuns.lower() == 'd':
                break


if __name__ == '__main__':
    main()
