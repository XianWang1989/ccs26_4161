
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options))
file = open("Class1.txt", "r")

resultsArray = []
lines = file.readlines()

for line in lines:
    new = line.strip()
    tempArray = new.split(',')
    name = tempArray.pop(0)
    scores = list(map(int, tempArray))
    resultsArray.append(scores)

if Option == "average score":
    total_scores = [sum(scores) for scores in resultsArray]
    average = sum(total_scores) / len(total_scores)
    print("Average score:", average)

file.close()
