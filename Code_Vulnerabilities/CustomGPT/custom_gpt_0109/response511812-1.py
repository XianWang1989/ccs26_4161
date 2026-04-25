
import string

# Define options and read user input
Options = ("alphabetical order", "highest to lowest", "average score")
Option = raw_input("Which order do you want to output? " + str(Options))

# Open the file and read lines
file = open("Class1.txt", "r")
lines = file.readlines()

# Initialize an empty list to store scores
all_scores = []

for line in lines:
    # Strip newlines and split by comma
    new = line.strip()
    tempArray = new.split(',')

    # Remove the name and extract scores
    name = tempArray.pop(0)  # Extract the name
    scores = list(map(int, tempArray))  # Convert remaining strings to integers
    all_scores.append(scores)  # Append scores to the list

# Calculate average if chosen
if Option == "average score":
    total_sum = 0
    count = 0

    for scores in all_scores:
        total_sum += sum(scores)  # Add sum of scores
        count += len(scores)  # Count total number of scores

    average = total_sum / count  # Calculate average
    print("Average score:", average)
