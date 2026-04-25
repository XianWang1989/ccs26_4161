
import string

# Options for output
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")  # Note: 'raw_input' is for Python 2.x

# Open the file containing class scores
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize an array to hold the scores
scores = []

# Process each line in the file
for line in lines:
    # Remove newline characters and split the line by comma
    clean_line = line.strip()
    tempArray = clean_line.split(',')

    # Extract scores and convert them to integers
    try:
        score_list = [int(tempArray[i]) for i in range(1, len(tempArray))]  # Skip the name
        scores.append(score_list)
    except ValueError:
        print(f"Invalid score found in line: '{line.strip()}'")

# Calculate average if requested
if Option == "average score":
    total_sum = 0
    count = 0

    for score_list in scores:
        total_sum += sum(score_list)
        count += len(score_list)

    if count > 0:
        average = total_sum / count
        print(f"Average score: {average:.2f}")
    else:
        print("No scores to average.")
