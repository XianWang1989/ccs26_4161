
import random

# Function to generate random math questions
def ask_questions():
    score = 0
    for _ in range(10):
        a, b = random.randint(1, 10), random.randint(1, 10)
        answer = input(f"What is {a} + {b}? ")
        if int(answer) == a + b:
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
            scores = file.readlines()
            print("\nLeaderboard:")
            for line in scores:
                print(line, end='')  # Avoids adding extra newlines
    except FileNotFoundError:
        print("No scores recorded yet.")

# Main program
def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
