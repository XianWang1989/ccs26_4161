
import string

# Options for sorting (not used in average calculation)
Options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(Options))

# Initialize lists to store scores
scores = []

# Read data from file
with open("Class1.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        # Strip newline characters and split by comma
        clean_line = line.strip()
        tempArray = clean_line.split(',')

        # The scores are the last three items in the array
        # Convert those to integers and append to scores list
        scores.append([int(num) for num in tempArray[1:]])

# Calculate average for each student
average_scores = []
for score_list in scores:
    avg = sum(score_list) / len(score_list)
    average_scores.append(avg)

# Calculate overall average
overall_average = sum(average_scores) / len(average_scores) if average_scores else 0

# Output results
print("Average scores for each student:", average_scores)
print("Overall average score:", overall_average)
