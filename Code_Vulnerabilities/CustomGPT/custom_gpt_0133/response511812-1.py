
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")
choices = ("Class 1", "Class 2", "Class 3")

# Open the file and read lines
with open("Class1.txt", "r") as file:
    lines = file.readlines()

resultsArray = []

# Process each line in the text file
for line in lines:
    # Remove newline characters and split by comma
    new1 = line.strip().split(',')

    # Convert scores to integers and store them with names in resultsArray
    name = new1[0]  # Name is the first element
    scores = [int(score) for score in new1[1:]]  # Convert rest to integers
    resultsArray.append((name, scores))

# Calculate the average score if the option is chosen
if Option == "average score":
    total_sum = 0
    total_count = 0

    # Loop through the results and calculate the total sum and count
    for name, scores in resultsArray:
        for score in scores:
            total_sum += score
            total_count += 1

    if total_count > 0:
        average = total_sum / total_count
        print(f"Average score: {average}")
    else:
        print("No scores to average.")
else:
    print("Selected option is not 'average score'.")
