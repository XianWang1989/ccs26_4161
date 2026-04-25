
import random

def ask_questions():
    score = 0
    for _ in range(10):
        # Generate two random numbers and an operator for a math question
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2  # Change to other operations as needed
        user_answer = int(input(f"What is {num1} + {num2}? "))

        if user_answer == answer:
            score += 1
    return score

def update_leaderboard(name, score):
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
    print(f"{name}, your score is: {score} out of 10")

    update_leaderboard(name, score)
    print("Current leaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
