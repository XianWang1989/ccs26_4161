
import random

def ask_questions():
    score = 0
    questions = [
        ("What is 5 + 3?", 8),
        ("What is 10 - 4?", 6),
        ("What is 3 * 7?", 21),
        ("What is 15 / 3?", 5),
        ("What is 9 + 1?", 10),
        ("What is 4 * 2?", 8),
        ("What is 100 - 45?", 55),
        ("What is 6 + 7?", 13),
        ("What is 2 * 5?", 10),
        ("What is 12 / 4?", 3)
    ]

    for question, answer in random.sample(questions, 10):
        user_answer = int(input(question + " "))
        if user_answer == answer:
            score += 1

    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as f:
            print("\nLeaderboard:")
            print(f.read())
    except FileNotFoundError:
        print("No scores recorded yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"{name}, your score is: {score} out of 10")
    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
