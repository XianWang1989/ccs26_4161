
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output?" + str(Options))
file = open("Class1.txt", "r")
lines = file.readlines()

# Initialize an array to store scores
scores = []

for line in lines:
    new_line = line.strip()
    tempArray = new_line.split(',')
    name = tempArray[0]  # Get the name
    scores_list = list(map(int, tempArray[1:]))  # Convert the rest to integers
    scores.append(scores_list)  # Append the scores to the scores list

if Option == "average score":
    averages = []
    for score in scores:
        average = sum(score) / len(score)  # Calculate average for each list
        averages.append(average)  # Store the averages
    print("Averages for each student:", averages)
