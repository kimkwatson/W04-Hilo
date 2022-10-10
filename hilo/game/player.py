# HiLo W04
# Author: Kim Watson


class Player():
    """A person who plays the game.

    The responsibility of the Player is to keep track of guesses and points.

    Attributes:
    points (int): The total points.
    """

    def __init__(self):

        self.points = 300 

    def guess(self):
        """Returns the player's guess for the current round of play.
        
        Args:
            self (Player): An instance of Player."""

        return input(f"Higher or lower? (h/l) ")

    def increment_points(self):
        """Increments the player's score for the current round of play.

        Args:
            self (Player): An instance of Player.
        """
        
        self.points += 100

    def decrement_points(self):
        """Decrements the player's score for the current round of play.

        Args:
            self (Player): An instance of Player.
        """
        
        self.points -= 75

    def get_score(self):
        """Returns the player's score.

        Args:
            self (Player): An instance of Player.
        """
        return self.points 
        
