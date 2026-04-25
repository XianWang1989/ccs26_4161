
import random

def ask_questions():
    score = 0
    for i in range(10):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = input(f"What is {num1} + {num2}? ")
        if int(answer) == num1 + num2:
            score += 1
    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("No scores yet!")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"Your score: {score} out of 10")

    save_score(name, score)
    print("Leaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
