
# Import necessary libraries
import string

# Define the options for output
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")
file = open("Class1.txt", "r")

# Read the lines from the file
lines = file.readlines()
file.close()

# Initialize a list to store the scores
scores = []

# Process each line
for line in lines:
    # Strip newlines and split by comma
    new_line = line.strip()
    tempArray = new_line.split(',')

    # Extract scores as integers
    scores.append([int(score) for score in tempArray[1:]])

# Calculate the average if the option is selected
if Option == "average score":
    # Sum and count scores
    total_scores = [sum(score) for score in scores]
    average = sum(total_scores) / len(total_scores)
    print("Average score:", average)
