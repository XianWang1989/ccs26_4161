
import random

def ask_questions():
    score = 0
    for _ in range(10):
        # Generate two random numbers
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        # Ask the user for the answer
        answer = input(f"What is {num1} + {num2}? ")
        # Check if the answer is correct
        if int(answer) == num1 + num2:
            score += 1
    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def display_scores():
    try:
        with open("leaderboard.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No scores yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"{name}, your score is {score} out of 10.")

    # Save the score to the leaderboard file
    save_score(name, score)

    # Display the leaderboard
    print("\nLeaderboard:")
    display_scores()

if __name__ == "__main__":
    main()
