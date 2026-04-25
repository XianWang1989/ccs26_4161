
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")

file = open("Class1.txt", "r")
lines = file.readlines()
resultsArray = []

for line in lines:
    new_line = line.strip()  # Remove newline characters
    tempArray = new_line.split(',')

    # Extracting name and scores
    name = tempArray.pop(0)
    scores = list(map(int, tempArray))  # Convert strings to integers
    resultsArray.append(scores)

# Calculating average
if Option == "average score":
    total_scores = [sum(scores) for scores in resultsArray]  # Sum each list of scores
    average = sum(total_scores) / (len(total_scores) * len(scores))  # Calculate overall average
    print("Average score:", average)

file.close()
