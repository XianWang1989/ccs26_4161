
import random

def ask_questions():
    score = 0
    questions = [
        ("What is 2 + 2?", 4),
        ("What is 3 * 3?", 9),
        ("What is 10 - 7?", 3),
        ("What is 8 / 4?", 2),
        ("What is 5 + 7?", 12),
        ("What is 6 * 2?", 12),
        ("What is 9 - 4?", 5),
        ("What is 3 * 7?", 21),
        ("What is 12 / 3?", 4),
        ("What is 15 - 5?", 10)
    ]

    random.shuffle(questions)

    for question, answer in questions:
        user_answer = input(f"{question} ")
        if int(user_answer) == answer:
            score += 1

    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print("\nLeaderboard:")
            print(file.read())
    except FileNotFoundError:
        print("No scores yet!")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"{name}, your score is: {score} out of 10")

    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
