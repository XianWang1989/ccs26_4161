
import string

# Options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + "\n")

# File reading
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize a list to store the scores
scores = []

# Process each line in the file
for line in lines:
    # Strip newline characters and split by comma
    temp_array = line.strip().split(',')

    # Append scores to the list (converting them to integers)
    scores.append([int(score) for score in temp_array[1:]])

# Calculate average if the chosen option is "average score"
if option == "average score":
    # Flatten the scores list and calculate the average
    all_scores = [score for sublist in scores for score in sublist]
    average = sum(all_scores) / len(all_scores)
    print(f"Average score: {average:.2f}")
