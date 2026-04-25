
import string

# Define options for the user
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")
file_name = "Class1.txt"

# Initialize variables
total_scores = []
num_scores = 0

# Open the file and read lines
with open(file_name, "r") as file:
    lines = file.readlines()

# Process each line in the file
for line in lines:
    # Remove newline characters and split by comma
    cleaned_line = line.strip()
    temp_array = cleaned_line.split(',')

    # Extract scores and convert them to integers
    scores = list(map(int, temp_array[1:]))  # take everything except the name and convert to int
    total_scores.extend(scores)  # accumulate scores
    num_scores += len(scores)  # keep track of total number of scores

# Calculate and print average if the option was chosen
if option == "average score":
    if num_scores > 0:  # Prevent division by zero
        average = sum(total_scores) / num_scores
        print("Average score:", average)
    else:
        print("No scores found.")
