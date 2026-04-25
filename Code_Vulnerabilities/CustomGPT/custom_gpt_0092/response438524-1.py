
import random

def ask_questions():
    score = 0
    for _ in range(10):
        # Generate two random numbers for the question
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        answer = int(input(f"What is {num1} + {num2}? "))
        if answer == num1 + num2:
            score += 1
    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file: # 'a' to append to the file
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No scores recorded yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    print("Score saved!")
    print("Leaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
