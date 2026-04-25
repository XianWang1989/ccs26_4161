
import random

def ask_questions():
    score = 0
    for _ in range(10):  
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2  # Change this to any math operation you'd like
        user_answer = int(input(f"What is {num1} + {num2}? "))  
        if user_answer == answer:
            score += 1
    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name}:{score} out of 10\n")  # Save the score to the file

def display_leaderboard():
    with open("leaderboard.txt", "r") as f:
        print(f.read())  # Display the contents of the leaderboard file

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    print(f"{name}, your score is {score} out of 10.")

    save_score(name, score)  # Save the score to the leaderboard file
    print("\nLeaderboard:")
    display_leaderboard()  # Display the leaderboard

if __name__ == "__main__":
    main()
