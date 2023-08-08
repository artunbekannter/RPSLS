from . import db


class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
        self.score = 0
        self.computer_score = 0

    def choose(self, choice):
        self.choice = choice


class MatchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_choice = db.Column(db.String(50), nullable=False)
    computer_choice = db.Column(db.String(50), nullable=False)
    result = db.Column(db.String(50), nullable=False)

    def __init__(self, player_choice, computer_choice, result):
        self.player_choice = player_choice
        self.computer_choice = computer_choice
        self.result = result
