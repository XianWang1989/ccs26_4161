
import random

# Initialize the leaderboard file
leaderboard_file = 'leaderboard.txt'

def ask_math_question():
    # Generate two random numbers and a random operation
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    question = f"What is {num1} {operation} {num2}? "
    return eval(f"{num1} {operation} {num2}"), question  # Calculate the answer

# Start of the program
name = input("Enter your name: ")
score = 0

# Ask 10 math questions
for _ in range(10):
    answer, question = ask_math_question()
    user_answer = int(input(question))
    if user_answer == answer:
        score += 1

# Save the user's score to the leaderboard file
with open(leaderboard_file, 'a') as file:
    file.write(f"{name}:{score} out of 10\n")

# Display the leaderboard
print("\nLeaderboard:")
with open(leaderboard_file, 'r') as file:
    for line in file:
        print(line.strip())  # Strip newline characters for cleaner output

# Note: To print without spaces, use commas in the print statements
print(f"{name}:{score} out of 10")
