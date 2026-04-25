
import string

# Define options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")

# Initialize an empty list to store scores
scores = []

# Read data from the file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Process each line
for line in lines:
    line = line.strip()  # Remove newline characters
    temp_array = line.split(',')  # Split by comma
    # Append scores to the scores list
    scores.append([int(x) for x in temp_array[1:]])  # Convert scores to integers

# Calculate averages
if option == "average score":
    average_scores = []
    for score_list in scores:
        average = sum(score_list) / len(score_list)  # Calculate average
        average_scores.append(average)
    print("Average scores:", average_scores)
