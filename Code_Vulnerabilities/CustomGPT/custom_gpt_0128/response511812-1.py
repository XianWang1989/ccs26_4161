
import string

# Options menu for output choice
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

file = open("Class1.txt", "r")

# Initialize lists to store scores
scores = []

# Read lines from the file
lines = file.readlines()
for line in lines:
    # Remove newline and strip whitespace
    new_line = line.strip()
    # Split the line into components
    temp_array = new_line.split(',')

    # Get scores as integers and store them
    scores.append([int(score) for score in temp_array[1:]])

# Calculate averages if the selected option is "average score"
if option == "average score":
    # Calculate average for each student
    averages = [sum(score_list) / len(score_list) for score_list in scores]

    # Print the averages
    for i, avg in enumerate(averages):
        print(f"Average score for {temp_array[0]}: {avg}")
