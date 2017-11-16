import random

class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

class CardDeck:
  values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
  suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

  def __init__(self):
    self.set_deck()

  def get_deck(self):
    return self.cards

  def set_deck(self):
    self.cards = []
    # for i in range(len(CardDeck.values)):
    #   for j in range(len(CardDeck.suits)):
    #     card = Card(CardDeck.values[i], CardDeck.suits[j])
    #     self.cards.append(card)
    for value in CardDeck.values:
      for suit in CardDeck.suits:
        card = Card(value=value, suit=suit)
        self.cards.append(card)

  def shuffle_card(self):
    counter = len(self.cards)
    while counter > 0:
      index = random.randint(0, counter)
      counter -= 1
      temp = self.cards[counter]
      self.cards[counter] = self.cards[index]
      self.cards[index] = temp
