
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options))

file = open("Class1.txt", "r")
lines = file.readlines()
file.close()

# List to keep track of all scores
all_scores = []

# Process each line in the file
for line in lines:
    line = line.strip()  # Remove any whitespace or new line characters
    tempArray = line.split(',')  # Split the line into an array by commas

    # Skip the name and just take the scores
    scores = [int(score) for score in tempArray[1:]]  # Convert score strings to integers
    all_scores.append(scores)  # Add this list of scores to all_scores

# Compute the average score if the user selected that option
if Option == "average score":
    total_sum = 0
    count = 0

    # Calculate the total sum and count of scores
    for scores in all_scores:
        total_sum += sum(scores)  # Sum of scores for this entry
        count += len(scores)       # Count of scores

    # Calculate the average from the total sum and count
    average = total_sum / count if count > 0 else 0
    print(f"Average score: {average}")

