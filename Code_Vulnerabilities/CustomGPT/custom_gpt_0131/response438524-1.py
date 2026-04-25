
import random

def ask_questions():
    score = 0
    for _ in range(10):
        # Generate two random numbers for the question
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = int(input(f"What is {num1} + {num2}? "))

        if answer == num1 + num2:
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
        print("No scores recorded yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)

    print("\nLeaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
