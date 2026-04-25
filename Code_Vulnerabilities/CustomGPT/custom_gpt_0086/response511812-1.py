
import string

# Options for sorting or calculating
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")

# Opening the file to read class scores
file = open("Class1.txt", "r")
lines = file.readlines()

# List to store individual scores
all_scores = []

# Processing each line in the file
for line in lines:
    line = line.strip()  # Removing whitespace and newline
    tempArray = line.split(',')
    scores = list(map(int, tempArray[1:]))  # Convert scores to integers
    all_scores.append(scores)  # Add scores to all_scores

file.close()  # Close the file

# Calculate the average for each student
if Option == "average score":
    averages = []
    for scores in all_scores:
        average = sum(scores) / len(scores)  # Calculate the average
        averages.append(average)  # Store the average

    print("Averages:", averages)
