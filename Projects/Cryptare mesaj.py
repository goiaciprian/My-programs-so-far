import time

# Cryptare si decryptare


def countdown(t):
    print('Fereastra se va inchide in 3 secunde.')
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Goodbye!\n\n')


def start():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = input('Introdu un numar pentru cryptare:')
    neg = key
    if key.isdecimal() or key == neg and key not in alphabet and neg not in alphabet:  # Accepta numere negative
        key1 = int(key)
    else:
        print('Trebuie un numar.')
        start()

    def main():
        newmessage = ''

        message = input('Introdu mesajul:')

        for character in message:  # Cryptarea
            if character in alphabet:  # Sare peste simnolurile care nu sunt in alphabet
                position = alphabet.find(character)
                newposition = (position + key1) % 26
                newcaracther = alphabet[newposition]
                # print('The new character is ',newCaracther)
                newmessage += newcaracther
            else:
                newmessage += character

        print('Mesajul criptat este: ', newmessage)

        restart = input('Din nou?')  # Meniu pentru restart sau decryptare
        if restart == 'Da' or restart == "d" or restart == 'da':
            main()
        elif restart == 'NU' or restart == 'nu' or restart == 'n':
            dec = input('Vrei sa decryptezi?')
            if dec == 'da' or dec == 'Da' or dec == 'd':
                start()
            else:
                countdown(3)
                quit()
        else:
            countdown(3)
            quit()
    main()


if __name__ == '__main__':
    start()
