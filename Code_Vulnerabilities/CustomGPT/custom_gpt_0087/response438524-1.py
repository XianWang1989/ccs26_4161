
import random

# Function to ask maths questions
def ask_questions():
    score = 0
    for _ in range(10):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2  # Change this for different operations
        user_answer = int(input(f"What is {num1} + {num2}? "))
        if user_answer == answer:
            score += 1
    return score

# Function to save score to a file
def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

# Function to display the leaderboard
def display_leaderboard():
    print("\nLeaderboard:")
    try:
        with open("leaderboard.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No scores available.")

# Main program
def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    display_leaderboard()

# Run the program
if __name__ == "__main__":
    main()
