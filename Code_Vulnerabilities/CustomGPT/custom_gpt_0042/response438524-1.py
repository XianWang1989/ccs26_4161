
import random

# Function to ask 10 random math questions
def ask_questions():
    score = 0
    for i in range(10):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
        answer = int(input(f"What is {num1} + {num2}? "))
        if answer == correct_answer:
            score += 1
    return score

# Function to save score to leaderboard
def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

# Function to display the leaderboard
def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print("\nLeaderboard:")
            print(file.read())
    except FileNotFoundError:
        print("No scores recorded yet.")

# Main program
def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    display_leaderboard()

# Run the program
if __name__ == "__main__":
    main()
