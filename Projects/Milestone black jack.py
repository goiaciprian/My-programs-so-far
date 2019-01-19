""""

Joc de blackjack

"""


import random

suits = ('Inima rosie', 'Romb', 'Trefla', 'Inima neagra')
ranks = ('Doi', 'Trei', 'Patru', 'Cinci', 'Sase', 'Sapte', 'Opt', 'Noua', 'Zece', 'Valet', 'Dama', 'Rege', 'As')
values = {'Doi': 2, 'Trei': 3, 'Patru': 4, 'Cinci': 5, 'Sase': 6, 'Sapte': 7, 'Opt': 8,
          'Noua': 9, 'Zece': 10, 'Valet': 10, 'Dama': 10, 'Rege': 10, 'As': 11}

playing = True


class Card:

    """" Creeaza o singura carte"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' de ' + self.suit


class Deck:

    """ Creeaza un pachet de carti """

    def __init__(self):
        self.deck = []
        for suit in suits:  # creeaza pachetul
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:  # printeaza pachetul de carti
            deck_comp += '\n ' + card.__str__()
        return 'Deck-ul contine:' + deck_comp

    def shuffle(self):  # amesteca cartile
        random.shuffle(self.deck)

    def deal(self):  # extrage o singura carte
        single_card = self.deck.pop()
        return single_card


class Hand:

    """ Creeaza mana jucatorului / dealer-ului"""

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):  # adauga o carte in mana
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'As':
            self.aces += 1

    def adjust_for_aces(self):  # foloseste asus ca val 1 in loc de 10
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    """ Creeaza bet-urile si totalul de chip-uri"""

    def __init__(self, total=100):  # default chip-urile sunt 100
        self.total = total
        self.bet = 0

    def win_bet(self):  # daca castigi runda iti adauga suma pariata
        self.total += self.bet

    def lose_bet(self):  # daca pierzi iti scade suma pariata
        self.total -= self.bet


def take_bet(chips):

    """ In o valoare de la utilizator si o verifica daca e un numar si daca e mai mica ca totalul de chip-uri"""

    while True:
        try:
            chips.bet = int(input('Cat vrei sa pariezi?\n '))
        except ValueError:
            print('Introdu numai numere!')
        else:
            if chips.bet > chips.total:
                print("Scuze ai trecut de: ", chips.total)
            else:
                break


def hit(deck, hand):

    """ Adauga o carte in mana"""

    hand.add_card(deck.deal())
    hand.adjust_for_aces()


def hit_or_stand(deck, hand):

    """ Intreaba utilizatorul daca vrea sa loveasca sau sa astepte ; daca asteapta se trece la tura dealer-ului"""

    global playing

    while True:

        x = input('Vrei sa stai sau sa lovesti? ( Insert s or l)\n')

        if x[0].lower() == 'l':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Jucatorul asteapta. E randul dealer-ului')
            playing = False
        else:
            print('Introdu numai s sau l.')
            continue
        break


def show_some(player, dealer):

    """" Arata 1 carte din mana dealer-ului"""

    print("\nMana dealer-ului:")
    print(" <carte ascunsa>")
    print('', dealer.cards[1])
    print("\nMana jucatoruli:", *player.cards, sep='\n ')


def show_all(player, dealer):

    """ Arata cartile din mana jocatorului"""

    print("\nMana dealer-ului:", *dealer.cards, sep='\n ')
    print("Mana dealer-ului =", dealer.value)
    print("\nMana jucatorului:", *player.cards, sep='\n ')
    print("Mana jucatorului =", player.value)


def player_bust(player, dealer, chips):

    """" Printeaza cand jucatorul a trecu peste 21"""

    print('Jucator prins!')
    chips.lose_bet()


def player_win(player, dealer, chips):

    """" Printeaza cand jucatorul a castigat"""

    print('Jucatorul a castigat!')
    chips.win_bet()


def dealer_win(player, dealer, chips):

    """" Printeaza cand dealer-ul a castigat"""

    print('Dealer-ul a castigat')
    chips.lose_bet()


def dealer_bust(player, dealer, chips):

    """" Printeaza cand dealer-ul a trecur de 21"""

    print('Jucatorul a castigat!')
    chips.win_bet()


def push(player, dealer):

    """" Printeaza cand e egal"""

    print('Egalitate !')


print('Bun venit la BLACKJACK!!')

# Incepe jocul

while True:

    deck = Deck()
    deck.shuffle()  # Se creeaza si se amesteca deck-ul

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())  # Se creeaza mana si se dau doua carti jucatorului

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())  # Se creeaza mana si se dau doua carti dealer-ului

    players_chips = Chips()  # Se creeaza chip-urile jucatorului (se poate adauga un input)

    take_bet(players_chips)  # Cere jucatoruli suma pe care vrea sa o parieza

    show_some(player_hand, dealer_hand)  # Arata 1 carte a dealer-ului si cartile jucatorului

    while playing:  # Mentine tura jucatoruli pana cand acesta alege sa stea

        hit_or_stand(deck, player_hand)  # Alegerea jucatorului de a sta sau a lovi

        show_some(player_hand, dealer_hand)  # Arata 1 carte a dealer-ului si cartile jucatorului

        if player_hand.value > 21:  # verifica daca jucatorul are valoarea totala peste 21
            player_bust(player_hand, dealer_hand, players_chips)
            break  # Printeaza mana jucatorilui si a dealer-ului si termina jocul

    if player_hand.value <= 21:  # verifica daca jucatorul are valoarea totala mai mica de 21

        # aici de poate inlocui cu < 17 pentu modul soft
        while dealer_hand.value < player_hand.value:  # Verifica daca mana dealer-ului e mai mica decat a jucatorului
            hit(deck, dealer_hand)  # Adauga o carte in mana dealer-ului

        # arata toate cartile din mana jucatorului si a dealer-ului
        show_all(player_hand, dealer_hand)

        # se stabileste castigatorul
        if dealer_hand.value > 21:  # Dealer-ul are peste 21 --> Jucatorul castiga
            dealer_bust(player_hand, dealer_hand, players_chips)

        elif dealer_hand.value > player_hand.value:  # Dealer-ul are valoarea totala mai mare --> Dealer-ul castiga
            dealer_win(player_hand, dealer_hand, players_chips)

        elif dealer_hand.value < player_hand.value:  # Dealer-ul are valoarea totala mai mica --> Jucatorul castiga
            player_win(player_hand, dealer_hand, players_chips)

        else:  # Daca ambii au 21 este egal
            push(player_hand, dealer_hand)

    print(f"Ai : {players_chips.total} in total")  # Anunta jucatoril care chip-uri mai are

    new_game = input('Joci din nou? (d or n): ')  # input pentru inca o runda

    if new_game[0].lower() == 'd':  # incepe alta runda
        playing = True  # se stabileste prima tura a jucatorului
        continue  # se ia de la capat
    else:
        break  # se opreste jocul
