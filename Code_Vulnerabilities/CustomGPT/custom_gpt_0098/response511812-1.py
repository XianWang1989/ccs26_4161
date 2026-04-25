
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")
filename = "Class1.txt"

with open(filename, "r") as file:
    lines = file.readlines()

resultsArray = []

# Process each line in the file
for line in lines:
    line = line.strip()  # Remove leading/trailing whitespace
    tempArray = line.split(',')  # Split by comma
    name = tempArray.pop(0)  # Remove name and ignore it
    scores = list(map(int, tempArray))  # Convert scores to integers
    resultsArray.append(scores)  # Append the list of scores

# Calculate average if the selected option is "average score"
if Option == "average score":
    total_sum = 0
    count = 0

    for scores in resultsArray:
        total_sum += sum(scores)
        count += len(scores)

    if count > 0:  # Avoid division by zero
        average = total_sum / count
        print("Average score:", average)
    else:
        print("No scores to average.")
