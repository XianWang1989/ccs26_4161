
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")
file = open("Class1.txt", "r")

# Lists to hold the scores
scores_list = []

# Read the lines and process them
lines = file.readlines()
for line in lines:
    line = line.strip()  # Remove any surrounding whitespace
    tempArray = line.split(',')
    name = tempArray[0]  # Extract name
    scores = list(map(int, tempArray[1:]))  # Convert scores to integers
    scores_list.append(scores)

# Calculate the average if the option is selected
if Option == "average score":
    total_sum = 0
    total_count = 0

    # Summing the scores
    for scores in scores_list:
        total_sum += sum(scores)
        total_count += len(scores)

    average = total_sum / total_count if total_count > 0 else 0
    print("Average Score:", average)

file.close()  # Close the file
