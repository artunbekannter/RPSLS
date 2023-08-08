from flask import render_template, request, session
from . import app, db
from .classes import Player, MatchHistory
import random


@app.route("/", methods=["GET", "POST"])
def index():
    if "score" not in session:
        session["score"] = 0
        session["computer_score"] = 0

    if request.method == "POST":
        user_choice = request.form["user_choice"]
        computer_choice = random.choice(
            ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        )

        result = determine_winner(user_choice, computer_choice)
        update_score(result)

        match = MatchHistory(
            player_choice=user_choice,
            computer_choice=computer_choice,
            result=result,
        )
        db.session.add(match)
        db.session.commit()

        return render_template(
            "result.html",
            user_choice=user_choice,
            computer_choice=computer_choice,
            result=result,
            player_score=session["score"],
            computer_score=session["computer_score"],
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
        session["computer_score"] -= 1
    elif result == "Computer wins!":
        session["score"] -= 1
        session["computer_score"] += 1


@app.route("/results")
def display_results():
    # Query the database for all match history records
    match_history = MatchHistory.query.all()

    return render_template("results.html", match_history=match_history)
