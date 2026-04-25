
import string

# Options for the user
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + " ")

# Initialize variables
total_sum = 0
count = 0
scores = []

# Read data from the file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        # Remove newline characters and split by commas
        line = line.strip()
        tempArray = line.split(',')

        # Extract the name and scores
        name = tempArray[0]
        scores_list = list(map(int, tempArray[1:]))  # Convert scores to integers
        scores.append(scores_list)

        # Add to total sum and count
        total_sum += sum(scores_list)
        count += len(scores_list)

# If the selected option is to calculate the average score
if option == "average score":
    average = total_sum / count if count > 0 else 0
    print("Average score:", average)
