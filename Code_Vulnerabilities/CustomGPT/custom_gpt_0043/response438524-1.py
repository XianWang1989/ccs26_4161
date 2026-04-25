
import random

def ask_questions():
    score = 0
    for i in range(10):
        # Generate two random numbers for the math question
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2

        # Ask the question
        answer = input(f"What is {num1} + {num2}? ")

        # Check if the answer is correct
        if answer.isdigit() and int(answer) == correct_answer:
            score += 1

    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print("\nLeaderboard:")
            print(file.read())
    except FileNotFoundError:
        print("Leaderboard is empty.")

def main():
    name = input("What is your name? ")
    score = ask_questions()
    print(f"{name}, you scored {score} out of 10.")

    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
