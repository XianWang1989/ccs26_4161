
import string

# Options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

# Initialize list to hold all average scores
average_scores = []

# Open the file and read the contents
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Process each line
for line in lines:
    # Clean the line and split into components
    clean_line = line.strip()
    parts = clean_line.split(',')

    # Extract name and scores, converting scores to integers
    name = parts[0]
    scores = list(map(int, parts[1:]))  # Convert string scores to integers

    # Calculate the average for this student
    average = sum(scores) / len(scores) if scores else 0  # Avoid division by zero
    average_scores.append((name, average))  # Append a tuple of name and average score

# Output the averages based on the selected option
if option == "average score":
    for name, avg in average_scores:
        print(f"{name}: Average Score = {avg:.2f}")
