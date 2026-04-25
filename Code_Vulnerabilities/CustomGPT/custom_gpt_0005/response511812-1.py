
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")
choices = ("Class 1", "Class 2", "Class 3")
file = open("Class1.txt", "r")

# Reading lines and calculating averages
lines = file.readlines()
scores = []

for line in lines:
    stripped_line = line.strip()
    temp_array = stripped_line.split(',')
    name = temp_array.pop(0)  # Extract the name
    scores.append([int(score) for score in temp_array])  # Convert scores to integers

file.close()

if Option == "average score":
    total_scores = [0] * len(scores[0])  # Assuming all students have same number of scores
    for score_list in scores:
        for i in range(len(score_list)):
            total_scores[i] += score_list[i]

    average_scores = [total / len(scores) for total in total_scores]
    print("Average Scores:", average_scores)
