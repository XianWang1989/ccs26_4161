
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? (Options: {}) ".format(Options))
file = open("Class1.txt", "r")

# Initialize a list to hold results
results = []

# Read lines from file
lines = file.readlines()
file.close()

# Process each line from the file
for line in lines:
    # Strip whitespace and newline characters, then split by comma
    tempArray = line.strip().split(',')

    # Get the name
    name = tempArray[0]

    # Convert scores to integers
    scores = list(map(int, tempArray[1:]))

    # Append name and scores to results
    results.append((name, scores))

# Calculate averages if needed
if Option == "average score":
    for name, scores in results:
        average = sum(scores) / len(scores) if scores else 0
        print(f"{name}'s average score: {average:.2f}")
