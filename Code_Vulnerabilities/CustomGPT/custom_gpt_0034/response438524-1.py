
import random

def ask_questions():
    score = 0
    questions = [
        ("What is 1 + 1?", 2),
        ("What is 2 * 2?", 4),
        ("What is 3 - 1?", 2),
        ("What is 8 / 2?", 4),
        ("What is 5 + 3?", 8),
        ("What is 6 - 4?", 2),
        ("What is 9 / 3?", 3),
        ("What is 7 + 2?", 9),
        ("What is 10 - 5?", 5),
        ("What is 4 * 1?", 4),
    ]

    for question, answer in random.sample(questions, 10):
        user_answer = int(input(question + " "))
        if user_answer == answer:
            score += 1

    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name}:{score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No scores yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()

    print(f"{name}, your score is {score} out of 10.")
    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
