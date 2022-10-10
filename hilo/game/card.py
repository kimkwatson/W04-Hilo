# HiLo W04
# Author: Kim Watson


import random

class Card:
    """A card with a number (between 1 and 13) on it .

    The responsibility of Card is to keep track of which card is randomly drawn from a deck.
   
    Attributes:
        card (int): The number shown on the card drawn.
    """
    def __init__(self):
        """Constructs a new instance of Card with a card attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.card = 0
    
    def draw(self):
        """Generates a new random value for a new card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.card = random.randint(1, 13)
        return self.card
    
