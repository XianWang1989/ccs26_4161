
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")

choices = ("Class 1", "Class 2", "Class 3")
file = open("Class1.txt", "r")

# Initialize a list to hold all scores
scores = []

# Read and process the lines from the file
for line in file:
    # Strip newline characters and split by comma
    tempArray = string.strip(line, '\n').split(',')
    # Remove the name and convert the rest to integers
    scores.append([int(x) for x in tempArray[1:]])

file.close()

if Option == "average score":
    # Calculate averages for each student's scores
    averages = [sum(student_scores) / len(student_scores) for student_scores in scores]
    print("Average scores:", averages)
