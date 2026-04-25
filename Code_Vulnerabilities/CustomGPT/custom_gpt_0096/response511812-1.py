
import string

# Options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")
file = open("Class1.txt", "r")

# List to store the scores
scores = []

# Read lines from the file
lines = file.readlines()

# Process each line
for line in lines:
    line = line.strip()  # Remove newline and extra spaces
    temp_array = line.split(',')

    # Extract and convert scores to integers
    scores.append([int(score) for score in temp_array[1:]])  # Skip name

# Close the file
file.close()

# Calculate the average if the option is chosen
if option == "average score":
    total_sum = 0
    total_count = 0

    for score_list in scores:
        total_sum += sum(score_list)
        total_count += len(score_list)

    average = total_sum / total_count if total_count > 0 else 0
    print(f"Average score: {average}")
