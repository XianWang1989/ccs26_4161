
import random

def ask_questions():
    score = 0
    for _ in range(10):
        # Create random math questions
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2
        user_answer = int(input(f"What is {num1} + {num2}? "))

        if user_answer == answer:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was {answer}.")

    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def show_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print("\nLeaderboard:")
            print(file.read())
    except FileNotFoundError:
        print("No leaderboard found yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"\n{name}, your score is: {score} out of 10.")
    save_score(name, score)
    show_leaderboard()

if __name__ == "__main__":
    main()
