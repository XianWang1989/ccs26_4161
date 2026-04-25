
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

# Function to save the score to the leaderboard
def save_to_leaderboard(name, score):
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name}: {score} out of 10\n")

# Function to display the leaderboard
def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No scores recorded yet.")

# Main program
def main():
    name = input("Enter your name: ")
    score = ask_questions()

    save_to_leaderboard(name, score)
    print("Your score:", score, "out of 10")

    print("\nLeaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
