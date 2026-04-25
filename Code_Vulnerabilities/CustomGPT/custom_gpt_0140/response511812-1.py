
import string

# Options for output
Options = ("alphabetical order", "highest to lowest", "average score")
Option = raw_input("Which order do you want to output? " + str(Options))
file = open("Class1.txt", "r")

# Initialize lists to store results
scores = []

# Read and process lines from the file
lines = file.readlines()
for line in lines:
    # Strip newline characters and split by comma
    tempArray = line.strip().split(',')
    name = tempArray[0]

    # Convert scores to integers
    scores_list = list(map(int, tempArray[1:]))
    scores.append(scores_list)

# Calculate average if the option is selected
if Option == "average score":
    # Calculate average for each student's scores
    average_scores = [sum(score) / len(score) for score in scores]
    print("Average scores for each student:")
    for i, avg in enumerate(average_scores):
        print(f"Student {i + 1}: {avg:.2f}")
else:
    print("Other options not implemented.")

file.close()
