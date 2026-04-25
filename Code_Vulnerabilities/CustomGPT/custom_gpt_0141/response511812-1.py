
# Improved Code
import string

# Define available options
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")

# Open the file and read lines
file = open("Class1.txt", "r")
lines = file.readlines()
file.close()

# Initialize a list to hold the scores
all_scores = []

# Process each line in the file
for line in lines:
    # Clean the line and split into parts
    new_line = line.strip()  # Remove whitespace and newline characters
    temp_array = new_line.split(',')  # Split by comma
    name = temp_array[0]  # First part is the name
    scores = list(map(int, temp_array[1:]))  # Convert remaining parts to integers

    all_scores.append(scores)  # Store the scores for this line

    print(f"Scores for {name}: {scores}")  # Print the individual scores for reference

# When the user selected "average score"
if Option == "average score":
    # Calculate the average scores
    averages = []
    for index in range(len(all_scores[0])):  # Assuming all classes have the same number of scores
        sum_scores = sum(scores[index] for scores in all_scores)
        average = sum_scores / len(all_scores)
        averages.append(average)

    print(f"Average scores: {averages}")  # Print the calculated averages
