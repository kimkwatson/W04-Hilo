# HiLo W04
# Author: Kim Watson


from game.player import Player 
from game.card import Card

class Director:

    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        self.player: An instance of Player. A person who is playing the game.
        self.deck: An instance of Card. A deck from which the director draws cards.
        is_playing (boolean): Whether or not the game is being played.
        self.card_previous: Stores the value of the previous card drawn.
        self.card_current: Stores the value of the most recent card drawn.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.guess = ""
        self.card_previous = 0
        self.card_current = 0

        self.player = Player()
        self.deck = Card()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card_current = self.draw_card()

        while self.is_playing:
            self.card_previous = self.card_current
            print(f"The card is: {self.card_previous}")
            self.guess = self.player.guess()
            self.card_current = self.draw_card()
            print(f"The next card is: {self.card_current}")
            self.score()
            print(f"Your score is: {self.player.get_score()}")
            self.get_input()

    def draw_card(self):
        """Draws a card from the deck.

        Args:
            self (Director): An instance of Director.
        """
        card = self.deck.draw()
        if card == self.card_current:
            self.deck.draw()

        return card


    def score(self):
        """Determines if the player's guess is correct and updates the points.

        Args:
            self (Director): An instance of Director.
        """

        if (self.card_current < self.card_previous and self.guess == "l")\
        or (self.card_current > self.card_previous and self.guess == "h"):
            self.player.increment_points() 
        
        else:
             self.player.decrement_points()
        
    
    def get_input(self):
        """Asks the user if they want to guess again.

        Args:
            self (Director): An instance of Director.
        """

        if self.player.get_score() > 0:
            play_again = input(f"Play again? (y/n) ")
            self.is_playing = (play_again == "y")
        
        else:
            self.is_playing = False

    