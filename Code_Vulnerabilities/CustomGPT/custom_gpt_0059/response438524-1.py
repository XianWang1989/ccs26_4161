
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
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Leaderboard is empty.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"Your score: {score} out of 10")

    save_score(name, score)
    print("\nCurrent Leaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
