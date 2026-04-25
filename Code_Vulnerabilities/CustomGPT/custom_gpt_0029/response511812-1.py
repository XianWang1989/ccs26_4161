
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")
file = open("Class1.txt", "r")

# Initialize lists to store scores
scores = []

# Read lines and process
lines = file.readlines()
for line in lines:
    stripped_line = line.strip()  # Remove whitespace and newline
    tempArray = stripped_line.split(',')
    name = tempArray.pop(0)  # Remove the name for later use if needed
    # Convert scores to integers and store
    score_list = list(map(int, tempArray))  # Convert remaining items to integers
    scores.append(score_list)

file.close()  # Remember to close the file

# Calculate the average if the option is selected
if Option == "average score":
    all_scores = [score for sublist in scores for score in sublist]  # Flatten the list
    average = sum(all_scores) / len(all_scores) if all_scores else 0  # Calculate average
    print("Average score:", average)
