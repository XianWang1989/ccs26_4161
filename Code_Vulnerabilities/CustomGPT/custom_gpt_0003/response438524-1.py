
import random

def ask_questions():
    score = 0
    questions = [
        ("What is 2 + 2?", 4),
        ("What is 5 * 3?", 15),
        ("What is 10 - 4?", 6),
        ("What is 8 / 2?", 4),
        ("What is 3 + 7?", 10),
        ("What is 12 - 5?", 7),
        ("What is 5 * 6?", 30),
        ("What is 9 / 3?", 3),
        ("What is 6 + 9?", 15),
        ("What is 16 - 8?", 8)
    ]

    # Shuffle questions for randomness
    random.shuffle(questions)

    for question, answer in questions:
        user_answer = int(input(question + " "))
        if user_answer == answer:
            score += 1

    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    print("\nLeaderboard:")
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No scores recorded yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"{name}, your score is {score} out of 10")

    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
