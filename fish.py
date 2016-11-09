from sys import exit
import random
#adssadsadsadsad
def deleting_card(x):
    for i in fulldeck:
        if i == x:
            fulldeck.remove(i)
            break

deck_of_cards = []
i = 1
while len(deck_of_cards) < 13:
    i += 1
    deck_of_cards.append(i)
print deck_of_cards
fulldeck = []
for i in deck_of_cards:
    fulldeck.append(i)
    fulldeck.append(i)
    fulldeck.append(i)
    fulldeck.append(i)
print fulldeck

player_cards = []

card_one = random.choice(fulldeck)
deleting_card(card_one)
card_two = random.choice(fulldeck)
deleting_card(card_two)
card_three = random.choice(fulldeck)
deleting_card(card_three)
card_four = random.choice(fulldeck)
deleting_card(card_four)


player_cards.append(card_one)
player_cards.append(card_two)
player_cards.append(card_three)
player_cards.append(card_four)

print player_cards



print fulldeck


#print random.choice(to_four)
