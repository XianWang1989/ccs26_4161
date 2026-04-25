
import random

# Function to ask math questions
def ask_questions():
    score = 0
    for _ in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        user_answer = int(input(f"What is {a} + {b}? "))
        if user_answer == a + b:
            score += 1
    return score

# Function to save score to leaderboard
def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

# Function to display leaderboard
def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No scores yet.")

# Main program
def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"You scored: {score} out of 10")

    save_score(name, score)
    print("Leaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
