
import random

def ask_questions():
    score = 0
    num_questions = 10
    for i in range(num_questions):
        # Generate a simple math question (e.g., addition)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = int(input(f"What is {a} + {b}? "))

        # Check the answer and update the score
        if answer == a + b:
            score += 1
    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of {10}\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            leaderboard = file.read()
            print(leaderboard)
    except FileNotFoundError:
        print("No leaderboard found. Start by adding a score.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"{name}, you scored {score} out of 10.")

    save_score(name, score)
    print("Current leaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
