import random

class Card():

    def __init__(self):
        
        self.value = 0
    
    def draw(self):

        return random.randint(1, 13)
    
