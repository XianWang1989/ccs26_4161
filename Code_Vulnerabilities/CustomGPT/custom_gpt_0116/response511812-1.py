
import string

# Options for output order
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")

# Read the data from the file
file = open("Class1.txt", "r")
lines = file.readlines()

# Initialize variables to store total scores and count
total_scores = []
for line in lines:
    # Strip newline characters and split the line into components
    new_line = line.strip()
    tempArray = new_line.split(',')

    # Extract scores as integers and append to total_scores
    scores = list(map(int, tempArray[1:]))  # Convert score strings to integers
    total_scores.append(scores)

# Calculate average if the user selected "average score"
if Option == "average score":
    averages = []
    for scores in total_scores:
        if scores:  # Check if scores list is not empty
            avg = sum(scores) / len(scores)  # Calculate average
            averages.append(avg)
    print("Average scores: ", averages)

file.close()
