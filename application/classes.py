class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
        self.score = 0
        self.computer_score = 0

    def choose(self, choice):
        self.choice = choice
