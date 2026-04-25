
import random

def ask_questions():
    score = 0
    for i in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = int(input(f"What is {a} + {b}? "))
        if answer == a + b:
            score += 1
    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name}: {score} out of 10\n")

def display_scores():
    try:
        with open("leaderboard.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No scores available yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    print("Scores:")
    display_scores()

if __name__ == "__main__":
    main()
