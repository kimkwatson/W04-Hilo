# HiLo W04
# Author: Kim Watson

from game.player import Player 
from game.card import Card

class Director:
    
    def __init__(self):
        
        self.is_playing = True
        self.guess = ""
        self.is_correct = False
        self.card_previous = 0
        self.card_current = 0

        self.player = Player()
        self.deck = Card()

    def start_game(self):

        self.card_current = self.draw_card()

        while self.is_playing:
            self.card_previous = self.card_current
            print(f"The card is: {self.card_previous}")
            self.guess = self.get_guess()
            self.card_current = self.draw_card()
            print(f"The next card is: {self.card_current}")
            self.score()
            print(f"Your score is: {self.player.get_score()}")
            self.get_input()

    def draw_card(self):

        return self.deck.draw()
        
    def get_guess(self):

        self.player.guess = input(f"Higher or lower? (h/l) ")

    def score(self):

        if self.card_current < self.card_previous and self.guess == "l":
            self.is_correct = True
        elif self.card_current > self.card_previous and self.guess == "h":
            self.is_correct = True
        else:
            self.is_correct = False

        if self.is_correct:
            self.player.increment_points() 
        else:
            self.player.decrement_points()
    
    def get_input(self):

        if self.player.get_score() > 0:
            play_again = input(f"Play again? (y/n) ")
            self.is_playing = (play_again == "y")
        
        else:
            self.is_playing = False

    