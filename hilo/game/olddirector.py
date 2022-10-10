from game.card import Card
import random


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        drawn_cards (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        guess: User's input of "higher" or "lower".
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.drawn_cards = []
        self.is_playing = True
        self.guess = ""
        self.score = 0
        self.total_score = 300

        current_card = card.value()
        self.drawn_cards.append(card)
        print(f"Your card is: {card}")
        print(f"Your score is: {self.total_score}\n")

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        """Ask the user if they want to draw.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if self.total_score > 0:
            draw_card = input("Draw a card? [y/n] ")
            self.is_playing = (draw_card == "y")
            self.guess = input("Next card higher or lower(h/l)? ")
        
        else:
            self.is_playing = False
       
    def do_updates(self):
        """Draws another card and updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        new_card = card.value()
        self.drawn_cards.append(card)
        
        if
        self.score =
        self.total_score += self.score

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the card and the score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "
    
        print(f"Your card is: {card}")
        print(f"Your score is: {self.total_score}\n")
        
        self.is_playing == (self.score > 0)