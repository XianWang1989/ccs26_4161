
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")
file = open("Class1.txt", "r")

# Initialize variables
total_scores = []
lines = file.readlines()

# Process each line
for line in lines:
    new_line = line.strip()
    tempArray = new_line.split(',')
    name = tempArray[0]  # Name is the first element
    scores = list(map(int, tempArray[1:]))  # Convert scores to integers
    total_scores.append(scores)  # Append scores as list

# Average calculation if requested
if Option == "average score":
    for scores in total_scores:
        average = sum(scores) / len(scores)  # Calculate average
        print(f"Average score for {scores}: {average}")

file.close()
