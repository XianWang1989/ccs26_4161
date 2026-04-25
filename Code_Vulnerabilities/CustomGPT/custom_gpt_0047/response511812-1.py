
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options))
file = open("Class1.txt", "r")

lines = file.readlines()
resultsArray = []

# Process each line in the file
for line in lines:
    new_line = line.strip()  # Strip newline characters
    tempArray = new_line.split(',')  # Split by comma
    name = tempArray.pop(0)  # Get the name
    scores = list(map(int, tempArray))  # Convert score strings to integers
    resultsArray.append(scores)  # Append scores to resultsArray

# Calculate and print averages if the option is selected
if Option == "average score":
    total_sum = 0
    total_count = 0

    for scores in resultsArray:
        total_sum += sum(scores)  # Add scores to total sum
        total_count += len(scores)  # Count scores

    average = total_sum / total_count  # Calculate average
    print("Average score:", average)

file.close()  # Don’t forget to close the file
