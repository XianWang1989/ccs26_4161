
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options))  # Use input() for Python 3
file = open("Class1.txt", "r")

# Initialize variables
scores_list = []
lines = file.readlines()

for line in lines:
    # Strip newline and split by commas
    new = line.strip().split(',')
    # Extract scores as integers
    scores = list(map(int, new[1:]))
    scores_list.append(scores)

# Close the file
file.close()

if Option == "average score":
    total_scores = [sum(scores) for scores in scores_list]
    average = sum(total_scores) / len(total_scores) if total_scores else 0
    print("Average score:", average)
