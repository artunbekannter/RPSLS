from flask import render_template, redirect, url_for, request
from . import app
from .classes import Player
import random


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_choice = request.form["user_choice"]
        computer_choice = random.choice(
            ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        )

        result = determine_winner(user_choice, computer_choice)

        return render_template(
            "result.html",
            user_choice=user_choice,
            computer_choice=computer_choice,
            result=result,
        )

    return render_template("index.html")


def determine_winner(player_choice, computer_choice):
    win_combinations = {
        "Rock": ["Scissors", "Lizard"],
        "Paper": ["Rock", "Spock"],
        "Scissors": ["Paper", "Lizard"],
        "Lizard": ["Paper", "Spock"],
        "Spock": ["Rock", "Scissors"],
    }

    if player_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in win_combinations[player_choice]:
        return "You win!"
    else:
        return "Computer wins!"
