
import random

def ask_questions():
    score = 0
    questions = [
        ("What is 2 + 2?", 4),
        ("What is 5 - 3?", 2),
        ("What is 3 * 3?", 9),
        ("What is 10 / 2?", 5),
        ("What is 6 + 4?", 10),
        ("What is 12 - 7?", 5),
        ("What is 7 * 2?", 14),
        ("What is 15 / 3?", 5),
        ("What is 4 + 6?", 10),
        ("What is 8 - 3?", 5),
    ]

    for question, answer in random.sample(questions, 10):
        user_answer = int(input(question + " "))
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
        print("No leaderboard found.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    print("Your score:", score, "out of 10")
    print("\nLeaderboard:")
    display_leaderboard()

# Execute the program
if __name__ == "__main__":
    main()
