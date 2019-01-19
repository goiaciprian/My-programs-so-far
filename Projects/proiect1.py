def main():  # Functie

    while True:  # Creeaza un loop pana se indeplineste conditia, lungime numarului este 3
        numar = input('Introdu un numar de 3 cifre: ')  # Accepta input de la utilizator
        if numar.__len__() == 3 and numar.isdecimal():  # Verifica daca lungimeasi daca sunt introduse numere
            prima_parte = numar[:1]  # Selecteaza de la inceputul inputului pana la valoarea data, fara acea valoare
            ultima_parte = numar[2:]  # Selecteaza de la valoarea data pana la sfarsit
            print(f'Rezultatul este: {prima_parte + ultima_parte}')  # Printeaza rezultatul
            main()  # O ia de la capat


if __name__ == '__main__':  # Executa doar daca fisierul este executat direct
    main()
