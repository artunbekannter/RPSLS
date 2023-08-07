class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def choose(self, choice):
        self.choice = choice
