
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options))
file = open("Class1.txt", "r")

lines = file.readlines()
resultsArray = []

# Process each line in the file
for line in lines:
    line = line.strip()  # Remove newline characters
    tempArray = line.split(',')
    name = tempArray.pop(0)  # Get the name
    scores = list(map(int, tempArray))  # Convert scores to integers
    resultsArray.append(scores)  # Add to results

file.close()  # Always close the file

# Calculate the average score if the option is selected
if Option == "average score":
    total_scores = [sum(scores) for scores in resultsArray]
    average = sum(total_scores) / len(total_scores)
    print("Average score:", average)
