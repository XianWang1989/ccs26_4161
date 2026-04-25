
import random

def save_score_to_leaderboard(name, score):
    with open("leaderboard.txt", "a") as file:  # Open in append mode
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("No scores available yet.")

def ask_questions():
    score = 0
    for _ in range(10):  # Ask 10 questions
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        answer = number1 + number2
        user_answer = int(input(f"What is {number1} + {number2}? "))
        if user_answer == answer:
            score += 1
    return score

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"{name}, your score is {score} out of 10.")

    save_score_to_leaderboard(name, score)
    print("\nLeaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
