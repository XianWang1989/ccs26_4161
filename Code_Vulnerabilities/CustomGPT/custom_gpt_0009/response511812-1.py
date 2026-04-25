
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = raw_input("Which order do you want to output? " + str(Options) + ": ")
file = open("Class1.txt", "r")

lines = file.readlines()
results = []

# Process each line in the text file
for line in lines:
    stripped_line = line.strip()  # Remove newline characters
    tempArray = stripped_line.split(',')  # Split by comma
    name = tempArray[0]  # Name is the first element
    scores = list(map(int, tempArray[1:]))  # Convert scores to integers
    results.append(scores)  # Append scores to results list

if Option == "average score":
    total_sum = 0
    count = 0

    # Calculate the average
    for scores in results:
        total_sum += sum(scores)  # Sum of scores from each list
        count += len(scores)  # Count of each score

    average = total_sum / count if count > 0 else 0  # Avoid division by zero
    print("Average score: ", average)

file.close()
