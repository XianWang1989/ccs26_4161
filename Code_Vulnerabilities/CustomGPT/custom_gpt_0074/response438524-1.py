
import random

def ask_questions():
    score = 0
    questions = [
        ("What is 2 + 2?", 4),
        ("What is 5 * 6?", 30),
        ("What is 12 / 4?", 3),
        ("What is 10 - 7?", 3),
        ("What is 3 + 5?", 8),
        ("What is 9 - 3?", 6),
        ("What is 6 / 2?", 3),
        ("What is 8 * 1?", 8),
        ("What is 15 - 5?", 10),
        ("What is 7 + 2?", 9),
    ]

    # Shuffle the questions to ask 10 random ones
    random.shuffle(questions)

    for question, answer in questions[:10]:
        user_answer = input(f"{question} ")
        if int(user_answer) == answer:
            score += 1

    return score

def save_to_leaderboard(name, score):
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as f:
            print("\nLeaderboard:")
            print(f.read())
    except FileNotFoundError:
        print("No scores available yet.")

if __name__ == "__main__":
    name = input("Enter your name: ")
    score = ask_questions()
    save_to_leaderboard(name, score)
    display_leaderboard()
