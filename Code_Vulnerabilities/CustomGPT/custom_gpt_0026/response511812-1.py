
import string

# Prompt for output option
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")

# Open the file
file = open("Class1.txt", "r")
lines = file.readlines()
file.close()  # Always close the file

# Initialize list to collect scores
all_scores = []

# Process each line in the file
for line in lines:
    new_line = line.strip()  # Remove any leading/trailing whitespace
    tempArray = new_line.split(',')

    # Extract scores, convert to integers, and add to all_scores
    scores = list(map(int, tempArray[1:]))  # Convert score strings to integers
    all_scores.append(scores)

# Calculate average if the selected option is "average score"
if option == "average score":
    total_scores = [sum(scores) for scores in all_scores]  # Sum each student's scores
    average = sum(total_scores) / len(total_scores)  # Calculate the overall average
    print(f"Average score: {average}")
else:
    print("Selected option is not 'average score'.")
