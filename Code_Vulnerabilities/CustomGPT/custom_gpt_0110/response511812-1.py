
import string

Options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(Options) + ": ")
file = open("Class1.txt", "r")

# Initialize variables to hold scores
scores = []

# Read and process the lines from the file
lines = file.readlines()
for line in lines:
    new_line = line.strip()  # Remove whitespace and newline characters
    temp_array = new_line.split(',')
    scores.append([int(x) for x in temp_array[1:]])  # Convert scores to integers

file.close()

if option == "average score":
    # Calculate and print averages for each class
    for i in range(len(scores[0])):  # Assuming all classes have the same number of scores
        class_scores = [score[i] for score in scores]
        average = sum(class_scores) / len(class_scores)  # Calculate the average
        print(f"Average score for Class {i + 1}: {average}")
