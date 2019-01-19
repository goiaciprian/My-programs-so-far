#!usr/bin/env python


class CreditCard:
    """
    :type number: str
    :type expiredate: str
    :type securitycode: str

    """
    def __init__(self, number=None, expiredate=None, securitycode=None):
        self.number = number
        self.expiredate = expiredate
        self.securitycode = securitycode

    def __str__(self):
        if self.number is not None and self.expiredate is not None and self.securitycode is not None:
            return f'Numarul cardului este: {self.number} .\n'\
                f'Data de expirare este: {self.expiredate} .\n'\
                f'Codul de securitate este: {self.securitycode} .\n'
        else:
            return 'Nu sunt atribuite elemente specifice cardului.'

    def gencardnumber(self):
        if self.number is None:
            import random

            while True:
                gen_num = ''
                while len(gen_num) < 16:
                    ceva = random.randint(0, 9)
                    gen_num += str(ceva)
                gen_num15 = gen_num[:15]
                lista_elm_patrate = [int(i)*2 for i in gen_num15[::2]]
                loop = 0

                while loop < 2:
                    for cra in lista_elm_patrate:
                        if len(str(cra)) == 2:
                            for n, i in enumerate(lista_elm_patrate):
                                if len(str(i)) == 2:
                                    numar = str(i)
                                    rezultat = int(numar[0]) + int(numar[1])
                                    lista_elm_patrate[n] = rezultat
                                    loop += 1
                    break

                lista_elm_simple = [int(z) for z in gen_num15[1::2]]
                lista_elm_simple.extend(lista_elm_patrate)

                total_lista = 0
                for i in lista_elm_simple:
                    total_lista += i

                total = total_lista + int(gen_num[15])

                if total % 10 == 0:
                    self.number = str(gen_num)
                    return self.number
        else:
            return f'Numarul cardului a fost deja generat: {self.number}.'

    def genexpiredate(self):
        if self.expiredate is None:
            from datetime import date
            from random import randint
            today = date.today()
            current_year = today.year
            expire_month = randint(1, 12)
            expire_year = randint(current_year+2, current_year+4)
            dictionar = {'Month': str(expire_month), 'Year': str(expire_year)}
            self.expiredate = f"{dictionar['Month']}/{dictionar['Year']}"
            return self.expiredate
        else:
            return f'Data de expirare este deja generata: {self.expiredate}'

    def gensecuritycode(self):
        if self.securitycode is None:
            from random import randint
            code = ''
            while len(code) < 3:
                ceva = randint(0, 9)
                code += str(ceva)
            self.securitycode = str(code)
            return self.securitycode
        else:
            return f'Codul de securitate este deja generat: {self.securitycode}.'

    def validate(self):
        if self.number is not None:
            import re

            numar_card = str(self.number)
            lista_finala = re.findall(r'\S+', numar_card)
            input_string = None

            try:
                input_string = lista_finala[0] + lista_finala[1] + lista_finala[2] + lista_finala[3]
            except IndexError:
                try:
                    input_string = lista_finala[0]
                except IndexError:
                    pass

            string_final = input_string[:15]
            lista_elm_patrate = [int(i) * 2 for i in string_final[::2]]
            loop = 0

            while loop < 2:
                for cra in lista_elm_patrate:
                    if len(str(cra)) == 2:
                        for n, i in enumerate(lista_elm_patrate):
                            if len(str(i)) == 2:
                                numar = str(i)
                                rezultat = int(numar[0]) + int(numar[1])
                                lista_elm_patrate[n] = rezultat
                                loop += 1
                break
            lista_elem_simple = [int(z) for z in string_final[1::2]]
            lista_elem_simple.extend(lista_elm_patrate)
            total_lista = 0
            for i in lista_elem_simple:
                total_lista += i
            total = total_lista + int(input_string[15])
            if total % 10 == 0:
                return 'Numarul cardului este valid .'
            else:
                return 'Numarul cardului nu este valid.Nu il folositi .'
        else:
            return 'Cardul nu are nici un numar.'


if __name__ == '__main__':
    from os.path import expanduser, isfile
    from sys import argv
    sa = argv
    desktop = expanduser('~/Desktop')
    consoleuser = CreditCard()
    if sa[0] == 'card-class.py':
        from os import system
        system('start powershell /c card-class.py')
        print('Programul ruleaza din consola')
        mesaj = 'Comenzi:\n'\
                '-verf = verifica daca exista fisierul necesar\n' \
                '-read = printeaza datale din fisier\n' \
                '-info = printeaza datale cardului daca exista\n'\
                '-del = sterge fisierul\n' \
                '-open = deschide fisierul\n' \
                '-gen = genereaza un fisier cu datele necesare\n'\
                '-check = verifica numarul cardului\n'\
                '-exit = inchide programul\n'
        print(mesaj)
        while True:
            user = input('>>>')
            if user == '-verf':
                from os.path import isfile
                exista = isfile(desktop+'/cardinfo.txt')
                print('Fisierul exista\n' if exista else 'Fisierul nu exista.\n')
            elif user == '-exit':
                from sys import exit
                print('Programul se va inchide.\n')
                exit(1)
            elif user == '-info':
                if isfile(desktop+'/cardinfo.txt'):
                    with open(desktop+'/cardinfo.txt', 'r') as consolefile:
                        data = consolefile.read()
                    data_split = data.split()
                    lista_numere = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                    consoleuser.number = ''
                    consoleuser.expiredate = ''
                    consoleuser.securitycode = ''
                    for cuv in data_split:
                        if len(cuv) == 16:
                            for s in cuv:
                                consoleuser.number += s
                        elif len(cuv) == 6 or len(cuv) == 7 and '/' in cuv:
                            for r in cuv:
                                consoleuser.expiredate += r
                        elif len(cuv) == 3:
                            seccode = ''
                            for nmr in cuv:
                                if nmr in lista_numere:
                                    seccode += nmr
                            for l in seccode:
                                consoleuser.securitycode += l
                    print(consoleuser, end='\n')
                    print('Note: Datele gasite in fisier se atribuie obiectului.\n')
                else:
                    print('Fisierul nu exista.\n')
            elif user == '-read':
                if isfile(desktop+'/cardinfo.txt'):
                    with open(desktop+'/cardinfo.txt', 'r') as cardinf:
                        data = cardinf.read()
                    print('#'*7 + '\n' + data + '\n' + '#'*7)
                else:
                    print('Fisierul nu exista.\n')

            elif user == '-del':
                if isfile(desktop+'/cardinfo.txt'):
                    from os import remove
                    remove(desktop+'/cardinfo.txt')
                    print('Fisierul a fost sters.\n')
                else:
                    print('Fisierul nu exista.\n')

            elif user == '-check':
                print(consoleuser.validate(), end='\n')

            elif user == '-gen':
                if isfile(desktop+'/cardinfo.txt'):
                    print('Fisierul exista deja.\n')
                else:
                    with open(desktop+'/cardinfo.txt', 'w') as genfile:
                        consoleuser.genexpiredate()
                        genfile.writelines(f'Numarul cardului este: {consoleuser.gencardnumber()} .\n')
                        genfile.writelines("Data de expirare este: {} .\n".format(consoleuser.expiredate))
                        genfile.writelines(f'Codul de securitate este: {consoleuser.gensecuritycode()} .\n')
                        print('Fisier generat.\n')
            elif user == '-open':
                try:
                    from os import startfile
                    print('Se deschide fisierul ...\n')
                    startfile(desktop+'/cardinfo.txt')
                except FileNotFoundError:
                    print('Fisierul nu exista.\n')
            else:
                print('Comanda nu este inregistrata.')
                print('Foloseste una dintre comenzile de mai jos.')
                print(mesaj, end='\n')
    else:
        if isfile(desktop+'/cardinfo.txt'):
            usercard = CreditCard()
            with open(desktop+'/cardinfo.txt', 'r+') as cardinfo:
                data = cardinfo.read()
                lista_date = data.split()
                for elem in lista_date:
                    if 'Concluzie:' in lista_date:
                        pass
                    else:
                        if len(elem) == 16:
                            usercard.number = elem
                            cardinfo.writelines(f'\nVerificare numar card...\nConcluzie:\n{usercard.validate()}')
        else:
            from os import system
            try:
                system('start powershell /c python card-class.py')
            except Exception as e:
                print(e)
                system('start cmd /c python card-class.py')
