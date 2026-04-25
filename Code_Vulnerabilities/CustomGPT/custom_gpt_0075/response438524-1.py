
import random

def ask_questions():
    score = 0
    for _ in range(10):
        x, y = random.randint(1, 10), random.randint(1, 10)
        answer = int(input(f"What is {x} + {y}? "))
        if answer == x + y:
            score += 1
    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    with open("leaderboard.txt", "r") as f:
        print(f.read())

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    print("Your score:", score)
    print("Leaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
