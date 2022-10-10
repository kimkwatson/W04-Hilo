
from operator import is_


class Player():

    def __init__(self):

        self.guess = ""
        self.is_correct = False
        self.points = 300 

    def guess(self):

        self.guess = input(f"Higher or lower: (h/l)")
        return self.guess

    def increment_points(self):
        
        self.points += 100

    def decrement_points(self):
        
        self.points -= 75

    def get_score(self):
        return self.points 
        
