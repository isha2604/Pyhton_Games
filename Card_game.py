# CARD CLASS
# HAS 3 MAIN PROPERTIES SUIT, RANK, VALUE
# DECK CLASS 52 CARD CLASS
# CREATE PLAYER WHO WILL HOLD THE CARD CLASS

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __int__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)        # for adding multiple cards
        else:
            self.all_cards.append(new_cards)        # for adding single cards

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

new_deck = Deck()
#
# new_player = Player()

# Add a player
# new_player.__int__("Jose")
# print(f"The new player added name is {new_player}")

# Add card to a new player
# mycard = new_deck.deal_one()
# print(f"The dealt card is {mycard}")
#
# new_player.add_cards(mycard)
# print(f"The card added to new player is {new_player}")

# Add multiple card to player
# new_player.add_cards([mycard,mycard,mycard])
# print(f"Added multiple card {new_player}")

# Remove card from deck
# new_player.remove_one()
# print(new_player)

# print(new_deck.all_cards)
# first_card = new_deck.all_cards[0]
# print(first_card)

# prints all the cards
# for cards in new_deck.all_cards:
#     print(f"\nThe card is as follow: {cards}")

# shuffle cards
new_deck.shuffle()
# print(new_deck.all_cards[0])

# pop one card out
# print(new_deck.deal_one())

# check length of deck
# print(len(new_deck.all_cards))

# GAME SETUP
player_one = Player()
player_two = Player()
player_one.__int__("One")
player_two.__int__("Two")

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

# WHILE GAME ON

round_num = 0
while game_on:
    round_num +=1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print('Player One out of cards! Player two Wins!!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two out of cards! Player One Wins!!')
        game_on = False
        break

    # START A NEW ROUND
    # cards player will leave on table
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

# WHILE AT WAR
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:         # -1 always draws the last card
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:         # -1 always draws the last card
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print("WAR!")

            if len(player_one.all_cards) < 3:
                print("Player one unable to play war, player two wins!!")
                game_on = False
                break

            elif len(player_two.all_cards) < 3:
                print("Player two unable to play war, player One wins!!")
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
