
import random

def ask_questions():
    score = 0
    for _ in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = a + b
        user_answer = int(input(f"What is {a} + {b}? "))

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
        print("No scores yet.")

def main():
    name = input("What's your name? ")
    score = ask_questions()
    print(f"{name}, your score is {score} out of 10.")

    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
