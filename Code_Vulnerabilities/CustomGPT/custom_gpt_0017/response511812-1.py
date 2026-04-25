
import string

# Define options and prompt user
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + "\n")

# Read data from file
file = open("Class1.txt", "r")
lines = file.readlines()
file.close()

# Initialize variables for average calculation
total_scores = []
num_scores = 0

# Process each line
for line in lines:
    # Strip whitespace and split by commas
    cleaned_line = line.strip()
    temp_array = cleaned_line.split(',')

    # Append scores to the total_scores list
    scores = list(map(int, temp_array[1:]))  # Convert score strings to integers
    total_scores.append(scores)
    num_scores += len(scores)

# Calculate average score if selected
if option == "average score":
    total_sum = sum(sum(scores) for scores in total_scores)
    average = total_sum / num_scores
    print(f"Average score: {average}")
