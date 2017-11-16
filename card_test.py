import card_deck

my_deck = card_deck.CardDeck()

my_deck.shuffle_card()

cards = my_deck.get_deck()

print('The deck has {} cards'.format(len(cards)))
print('The top card is the {} of {}'.format(cards[0].value, cards[0].suit))
