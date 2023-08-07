from flask import render_template, request, session
from . import app
from .classes import Player
import random


@app.route("/", methods=["GET", "POST"])
def index():
    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":
        user_choice = request.form["user_choice"]
        computer_choice = random.choice(
            ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        )

        result = determine_winner(user_choice, computer_choice)
        update_score(result)

        return render_template(
            "result.html",
            user_choice=user_choice,
            computer_choice=computer_choice,
            result=result,
            score=session["score"],
        )

    return render_template("index.html")


def determine_winner(player_choice, computer_choice):
    win_combinations = {
        "Rock": ["Scissors", "Lizard"],
        "Paper": ["Rock", "Spock"],
        "Scissors": ["Paper", "Lizard"],
        "Lizard": ["Spock", "Paper"],
        "Spock": ["Scissors", "Rock"],
    }

    if player_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in win_combinations[player_choice]:
        return "You win!"
    else:
        return "Computer wins!"


def update_score(result):
    if result == "You win!":
        session["score"] += 1
    elif result == "Computer wins!":
        session["score"] -= 1
