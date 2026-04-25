
import random

def ask_questions():
    score = 0
    questions = [
        ("What is 2 + 2?", 4),
        ("What is 5 * 3?", 15),
        ("What is 10 - 6?", 4),
        ("What is 12 / 2?", 6),
        ("What is 7 + 8?", 15),
        ("What is 15 - 9?", 6),
        ("What is 3 * 3?", 9),
        ("What is 8 / 4?", 2),
        ("What is 9 + 1?", 10),
        ("What is 6 * 2?", 12)
    ]
    random.shuffle(questions)

    for question, answer in questions[:10]:
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
            print(f.read())
    except FileNotFoundError:
        print("No scores yet!")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"{name}, your score is: {score} out of 10")
    save_score(name, score)
    print("\nCurrent Leaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
