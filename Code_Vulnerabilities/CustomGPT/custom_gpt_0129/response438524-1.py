
import random

# Function to ask math questions and return score
def ask_questions():
    score = 0
    for _ in range(10):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
        user_answer = int(input(f"What is {num1} + {num2}? "))
        if user_answer == correct_answer:
            score += 1
    return score

# Function to save score to the leaderboard file
def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}:{score} out of 10\n")

# Function to display the leaderboard
def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            contents = file.read()
            print("Leaderboard:")
            print(contents)
    except FileNotFoundError:
        print("No scores available yet.")

# Main program
def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
