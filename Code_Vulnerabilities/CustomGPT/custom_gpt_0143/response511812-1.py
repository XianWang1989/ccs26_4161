
import string

# Define options
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))
choices = ("Class 1", "Class 2", "Class 3")

# Read data from the file
file = open("Class1.txt", "r")
lines = file.readlines()
file.close()  # Always close the file after reading

# Initialize an empty list for all scores
all_scores = []

# Process each line in the file
for line in lines:
    # Strip newline and split by commas
    cleaned_line = string.strip(line, '\n')
    temp_array = cleaned_line.split(',')

    # Extract scores and convert them to integers
    scores = [int(x) for x in temp_array[1:]]  # Convert scores to integers
    all_scores.append(scores)  # Add to the list of all scores
    print("Scores for {}: {}".format(temp_array[0], scores))

# Calculate average if option is "average score"
if option == "average score":
    total_scores = []

    # Flatten the list of score lists
    for scores in all_scores:
        total_scores.extend(scores)

    # Calculate the average
    if total_scores:
        average = sum(total_scores) / len(total_scores)
        print("Average score:", average)
    else:
        print("No scores available to calculate average.")
