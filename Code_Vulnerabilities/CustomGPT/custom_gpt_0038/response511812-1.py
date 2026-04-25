
import string

# Define options
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options))
filename = "Class1.txt"

# Initialize variables for the average calculation
total_scores = []
num_scores = 0

# Open the file and read the lines
with open(filename, "r") as file:
    lines = file.readlines()

# Process each line to extract scores
for line in lines:
    new_line = line.strip()  # Remove newline character
    tempArray = new_line.split(',')  # Split by comma
    name = tempArray[0]  # First element is the name
    scores = list(map(int, tempArray[1:]))  # Convert scores to integers

    # Append scores to the total_scores list
    total_scores.extend(scores)
    num_scores += len(scores)  # Count number of scores

# Calculate and print the average if the option is chosen
if Option == "average score":
    if num_scores > 0:
        average = sum(total_scores) / num_scores
        print(f"The average score is: {average:.2f}")
    else:
        print("No scores available to calculate average.")
