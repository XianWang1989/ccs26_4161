
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options))
file = open("Class1.txt", "r")

# Initialize variables for calculating averages
scores = []

# Read and process lines from the file
lines = file.readlines()
for line in lines:
    new_line = line.strip()
    tempArray = new_line.split(',')

    # Convert scores to integers and store them
    scores.append([int(score) for score in tempArray[1:]])

if Option == "average score":
    average_scores = [sum(score_list) / len(score_list) for score_list in scores]
    print("Average scores:", average_scores)

file.close()
