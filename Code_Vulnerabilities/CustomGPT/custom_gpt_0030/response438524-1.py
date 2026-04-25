
import random

def quiz():
    name = input("Enter your name: ")
    score = 0

    questions = [
        ("What is 5 + 3?", 8),
        ("What is 12 - 4?", 8),
        ("What is 6 x 7?", 42),
        ("What is 20 / 4?", 5),
        ("What is 15 + 10?", 25),
        ("What is 9 - 2?", 7),
        ("What is 3 x 3?", 9),
        ("What is 14 - 6?", 8),
        ("What is 8 + 7?", 15),
        ("What is 4 x 5?", 20)
    ]

    for question, answer in random.sample(questions, 10):
        user_answer = int(input(question + " "))
        if user_answer == answer:
            score += 1

    print(f"{name}, your score is: {score} out of 10")
    save_score(name, score)
    display_leaderboard()

def save_score(name, score):
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as f:
            print("\nLeaderboard:")
            print(f.read())
    except FileNotFoundError:
        print("No leaderboard exists yet.")

quiz()
