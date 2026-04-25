
import random

def ask_questions():
    score = 0
    for _ in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = int(input(f"What is {a} + {b}? "))
        if answer == a + b:
            score += 1
    return score

def save_to_leaderboard(name, score):
    with open('leaderboard.txt', 'a') as file:
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open('leaderboard.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("No scores recorded yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_to_leaderboard(name, score)
    print(f"{name}, your score is: {score} out of 10")
    print("\nLeaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
