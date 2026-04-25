
import random

# Function to ask math questions
def ask_questions():
    score = 0
    for _ in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = input(f"What is {a} + {b}? ")
        if int(answer) == a + b:
            score += 1
    return score

# Function to save score to a file
def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

# Function to display leaderboard
def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print("Leaderboard:")
            print(file.read())
    except FileNotFoundError:
        print("No scores yet!")

# Main program
def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    display_leaderboard()

# Call the main function
if __name__ == "__main__":
    main()
