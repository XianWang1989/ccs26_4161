
import string

# Define the options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))
file_path = "Class1.txt"

# Read the data from the file
with open(file_path, "r") as file:
    lines = file.readlines()

# Initialize a list to store the scores
scores = []

# Process each line to extract names and scores
for line in lines:
    # Strip newline and split by comma
    parts = line.strip().split(',')
    name = parts[0]

    # Convert the subsequent parts to integers
    scores_list = list(map(int, parts[1:]))
    scores.append((name, scores_list))

# Calculate averages if the selected option is "average score"
if option == "average score":
    averages = []
    for name, score_list in scores:
        average = sum(score_list) / len(score_list)
        averages.append((name, average))

    # Print the averages
    for name, avg in averages:
        print(f"{name}: {avg:.2f}")
