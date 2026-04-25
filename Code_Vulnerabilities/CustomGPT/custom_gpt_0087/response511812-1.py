
import string

# Options for sorting
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

# Dictionary to store scores
scores = []

# Read the file
with open("Class1.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()  # Remove newline characters
        tempArray = line.split(',')
        # Extract name and scores, converting scores to integers
        name = tempArray[0]
        score_list = list(map(int, tempArray[1:]))
        scores.append(score_list)

# Calculate average scores
if option == "average score":
    all_scores = []
    for score_list in scores:
        all_scores.extend(score_list)

    average = sum(all_scores) / len(all_scores)
    print("Average score:", average)
