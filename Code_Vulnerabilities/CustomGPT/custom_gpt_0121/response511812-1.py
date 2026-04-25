
import string

# Options for output
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + " ")

# Open the file and read lines
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize a list to store all scores
all_scores = []

# Process each line in the file
for line in lines:
    clean_line = line.strip()  # Remove trailing newline
    parts = clean_line.split(',')  # Split by comma
    name = parts[0]  # Extract name
    scores = list(map(int, parts[1:]))  # Convert scores to integers
    all_scores.append(scores)  # Append scores to the list

# Calculate and print the average if selected
if Option == "average score":
    total_sum = 0
    total_count = 0

    for scores in all_scores:
        total_sum += sum(scores)  # Sum each list of scores
        total_count += len(scores)  # Count total number of scores

    average = total_sum / total_count if total_count > 0 else 0
    print("Average score:", average)
