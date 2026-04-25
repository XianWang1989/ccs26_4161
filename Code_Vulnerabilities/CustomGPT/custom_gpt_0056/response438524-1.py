
import random

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print("Leaderboard:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No scores saved yet.")

def ask_questions():
    score = 0
    for _ in range(10):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = int(input(f"What is {num1} + {num2}? "))
        if answer == num1 + num2:
            score += 1
    return score

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"{name}, your score is {score} out of 10.")

    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
