import collections

# define a class, that is a named tuple, called Card. that has a rank and suit.
# a named tuple is one where each element can be accessed by a name instead of just an index. 
Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    # a list of all "ranks" in a deck of cards, 2 through 10 and J (Jack), Q (Queen), K (King), A (Ace). Total = 13 ranks. 
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")

    # .split() will split the string on the spaces and save the values inbetween (words/suits) inside a list called "suits".
    suits = "spades diamonds clubs hearts".split()

    # special initialize method used to assign attributes to objects on creation/instantiation. 
    # creating a list of "Card" tuples for every suit and every rank in the FrenchDeck class ex. (2, diamonds) or (K, hearts).
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    # returning the length of the list of cards in the FrenchDeck via the self._cards non-public instance variable.
    def __len__(self):
        return len(self._cards)
    
    # returning the card found at the given index position from the list of cards in the self._cards instance variable. 
    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
