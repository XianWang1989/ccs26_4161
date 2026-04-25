
import string

# Define your options
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

# Open the file
file = open("Class1.txt", "r")
lines = file.readlines()

# Prepare to store total scores and count
total_scores = []
sum_scores = 0

# Process each line from the file
for line in lines:
    # Strip the line of whitespace and split it into components
    new_line = line.strip()
    temp_array = new_line.split(',')

    # Get the name and their scores
    name = temp_array[0]
    scores = [int(score) for score in temp_array[1:]]  # Convert scores to integers

    # Append scores to total_scores
    total_scores.append(scores)

    # Calculate sum for this student's scores
    sum_scores += sum(scores)

# Calculate average if average option is chosen
if option == "average score":
    # Calculate the total number of scores
    total_number_of_scores = sum(len(scores) for scores in total_scores)
    average = sum_scores / total_number_of_scores if total_number_of_scores > 0 else 0
    print("Average score:", average)

# Close the file
file.close()
