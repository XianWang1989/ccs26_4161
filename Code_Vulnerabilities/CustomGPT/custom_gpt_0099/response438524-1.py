
import random

def ask_questions():
    score = 0
    for _ in range(10):
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        answer = num1 + num2
        user_answer = int(input(f"What is {num1} + {num2}? "))
        if user_answer == answer:
            score += 1
    return score

def save_to_leaderboard(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    print("\nLeaderboard:")
    with open("leaderboard.txt", "r") as file:
        print(file.read())

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"{name}, your score is: {score} out of 10")

    save_to_leaderboard(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
