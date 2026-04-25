
import string

# Options for output
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options))  # Change raw_input to input

# Read file
file = open("Class1.txt", "r")
lines = file.readlines()

# Initialize the list for scores
all_scores = []

# Process each line
for line in lines:
    # Strip whitespace and newlines, and split by commas
    tempArray = line.strip().split(',')
    # Extract scores
    scores = list(map(int, tempArray[1:]))  # Convert scores to integers
    all_scores.append(scores)

# Calculate average if the option is chosen
if Option == "average score":
    total_sum = 0
    total_count = 0

    # Sum scores
    for scores in all_scores:
        total_sum += sum(scores)
        total_count += len(scores)

    # Calculate the average
    if total_count > 0:
        average = total_sum / total_count
        print("Average score:", average)
    else:
        print("No scores to average.")

file.close()
