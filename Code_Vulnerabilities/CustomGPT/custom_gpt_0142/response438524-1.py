
import random

def ask_questions():
    score = 0
    for _ in range(10):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2
        user_answer = int(input(f"What is {num1} + {num2}? "))  # Ask the question
        if user_answer == answer:
            score += 1
    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:  # Open leaderboard.txt in append mode
        file.write(f"{name}: {score} out of 10\n")  # Write the score to the file

def display_leaderboard():
    print("\nLeaderboard:")
    with open("leaderboard.txt", "r") as file:
        for line in file:
            print(line, end="")  # Print without adding extra newlines

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"\nYour score: {score} out of 10")
    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
