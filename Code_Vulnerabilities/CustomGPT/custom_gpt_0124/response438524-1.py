
import random

def ask_questions():
    score = 0
    for _ in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        correct_answer = a + b

        # Ask the question
        answer = int(input(f"What is {a} + {b}? "))

        # Check the answer
        if answer == correct_answer:
            score += 1

    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as f:
            print("\nLeaderboard:")
            for line in f:
                print(line, end="")
    except FileNotFoundError:
        print("No scores yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
