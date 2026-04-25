
import string

# Options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

# Initialize lists to store results
scores = []

# Read from the file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Process each line
for line in lines:
    # Strip newline and split by comma
    new_str = line.strip()
    temp_array = new_str.split(',')

    # Extract name and scores
    name = temp_array[0]
    scores_list = list(map(int, temp_array[1:]))  # Convert scores to integers

    # Append scores to the main scores list
    scores.append(scores_list)

# Calculate average if option selected
if option == "average score":
    total_sum = 0
    total_count = 0

    for score_list in scores:
        total_sum += sum(score_list)
        total_count += len(score_list)

    # Calculate average
    if total_count > 0:
        average = total_sum / total_count
    else:
        average = 0

    print("Average score:", average)
