
import random

def ask_questions():
    score = 0
    questions = [
        ("What is 5 + 3?", 8),
        ("What is 10 - 2?", 8),
        ("What is 6 * 7?", 42),
        ("What is 20 / 4?", 5),
        ("What is 9 + 10?", 19)
    ]

    random.shuffle(questions)

    for question, answer in questions[:10]:
        user_answer = int(input(question + " "))
        if user_answer == answer:
            score += 1

    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}:{score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No scores yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"{name}, your score is {score} out of 10.")

    save_score(name, score)
    print("Leaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
