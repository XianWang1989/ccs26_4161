
import string

# Define the available options
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")

# Open the file and read lines
file = open("Class1.txt", "r")
lines = file.readlines()

# Prepare a list to store scores
scores = []

# Process each line in the file
for line in lines:
    line = line.strip()  # Remove newline characters
    tempArray = line.split(',')  # Split by commas
    name = tempArray[0]  # Extract name
    # Convert scores to integers and add to scores list
    scores.append([int(score) for score in tempArray[1:]])

# Calculate average if selected
if Option == "average score":
    total_sum = 0
    total_count = 0

    # Iterate through each score list
    for score_list in scores:
        total_sum += sum(score_list)
        total_count += len(score_list)

    average = total_sum / total_count if total_count > 0 else 0
    print("Average score:", average)

file.close()  # Don't forget to close the file
