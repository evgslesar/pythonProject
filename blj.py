import random

suits = ('Червы', 'Бубны', 'Пики', 'Трефы')
ranks = ('Двойка', 'Тройка', 'Четвёрка', 'Пятёрка', 'Шестёрка', 
'Семёрка', 'Восьмёрка', 'Девятка', 'Десятка', 
'Валет', 'Дама', 'Король', 'Туз')
values = {'Двойка':2, 'Тройка':3, 'Четвёрка':4, 'Пятёрка':5, 
'Шестёрка':6, 'Семёрка':7, 'Восьмёрка':8, 'Девятка':9, 
'Десятка':10, 'Валет':10, 'Дама':10, 'Король':10, 'Туз':11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' ' + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'В колоде находятся карты: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Туз':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('Сколько фишек вы хотите поставить? '))

        except:
            print('Извините, введите число, пожалуйста')

        else:
            if chips.bet > chips.total:
                print('Извините, недостаточно фишек. \
                Доступное количество фишек: {}'.format(chips.total))
            else:
                break

def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input('Взять дополнительную карту (hit) или остаться при \
            текущих картах (stand). Введите h или s.')

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print('Игрок остаётся при своих картах. Ход дилера')
            playing = False

        else:
            print('Ответ непонятен. Введите h или s.')
            continue
        break

def player_busts(player, dealer, chips):
    print('Превышение суммы 21 для игрока')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Игрок выиграл')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Игрок выигралю Дилер превысил 21')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('Дилер выиграл!')
    chips.lose_bet()

def push(player, dealer, chips):
    print('Ничья!')


while True:

    print('')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    # show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        # show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

if player_hand.value <= 21:

    while dealer_hand.value < 17:
        hit(deck,dealer_hand)

    # show_some(player_hand, dealer_hand)

    if dealer_hand.value > 21:
        dealer_busts(player_hand,dealer_hand,player_chips)
    elif dealer_hand.value > player_hand.value:
        dealer_wins(player_hand,dealer_hand,player_chips)
    elif dealer_hand.value < player_hand.value:
        player_wins(player_hand,dealer_hand,player_chips)
    else:
        push(player_hand,dealer_hand)

    print('Количество фишек игрока {}'.format(player_chips.total))

    new_game = input('Хотите сфграть снова? y или n')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Спасибо за игру')
        break

    break


