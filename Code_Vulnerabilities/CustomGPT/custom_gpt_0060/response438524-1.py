
import random

def ask_questions():
    score = 0
    for i in range(10):
        # Generate two random numbers and a random operation
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-'])

        if operation == '+':
            answer = num1 + num2
        else:
            answer = num1 - num2

        # Ask the question
        user_answer = input(f"What is {num1} {operation} {num2}? ")

        # Check the answer
        if user_answer.isdigit() and int(user_answer) == answer:
            score += 1

    return score

def save_to_leaderboard(name, score):
    with open("leaderboard.txt", "a") as f:  # Append to file
        f.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as f:
            print("\nLeaderboard:")
            print(f.read())  # Print all contents of the file
    except FileNotFoundError:
        print("No leaderboard entries yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_to_leaderboard(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
