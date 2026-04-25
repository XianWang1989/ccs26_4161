
import string

# Define options
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + " ")

# Open the file and read lines
file = open("Class1.txt", "r")
lines = file.readlines()
file.close()

# Initialize a list to store results
resultsArray = []

# Process each line
for line in lines:
    new_line = line.strip()
    tempArray = new_line.split(',')

    # Extract the name and scores
    name = tempArray[0]
    scores = list(map(int, tempArray[1:]))  # Convert scores to integers

    # Store the scores along with the name
    resultsArray.append((name, scores))

# Calculate the average scores
if Option == "average score":
    for name, scores in resultsArray:
        average = sum(scores) / len(scores)  # Calculate the average
        print(f"{name}: Average score = {average}")
