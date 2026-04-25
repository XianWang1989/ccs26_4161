
import random

def ask_questions():
    score = 0
    for i in range(10):
        # Generate two random numbers for the question
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2  # Change this for different operations
        user_answer = int(input(f"What is {num1} + {num2}? "))

        if user_answer == answer:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was {answer}.")

    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:  # Open the file in append mode
        file.write(f"{name}: {score} out of 10\n")  # Format the line

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print("\nLeaderboard:")
            for line in file:
                print(line.strip())  # Remove extra newline characters
    except FileNotFoundError:
        print("No scores yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()

    print(f"{name}, you scored {score} out of 10.")

    save_score(name, score)  # Save the score to the file
    display_leaderboard()     # Display the leaderboard

if __name__ == "__main__":
    main()
