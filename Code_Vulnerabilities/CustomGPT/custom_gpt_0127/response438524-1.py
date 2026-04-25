
import random

def ask_questions():
    score = 0
    questions = [
        ("What is 2 + 2?", 4),
        ("What is 3 * 3?", 9),
        ("What is 10 - 6?", 4),
        ("What is 5 + 7?", 12),
        ("What is 8 / 2?", 4),
        ("What is 3 + 5?", 8),
        ("What is 6 * 7?", 42),
        ("What is 9 - 4?", 5),
        ("What is 15 / 3?", 5),
        ("What is 12 + 8?", 20),
    ]
    random.shuffle(questions)

    for question, answer in questions[:10]:
        user_answer = int(input(f"{question} "))
        if user_answer == answer:
            score += 1

    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No scores recorded yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
