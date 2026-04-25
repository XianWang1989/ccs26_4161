
import string

# Prompt for order option
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))
file = open("Class1.txt", "r")

# Initialize variables for averages
total_scores = []
loopcount = len(file.readlines())
file.seek(0)  # Reset file pointer to the start

# Read and parse lines from the file
for line in file:
    cleaned_line = line.strip()
    temp_array = cleaned_line.split(',')

    # Get scores as integers
    scores = list(map(int, temp_array[1:]))  # Convert score strings to integers
    total_scores.append(scores)  # Append the scores to the list

file.close()

if option == "average score":
    averages = []
    for scores in total_scores:
        average = sum(scores) / len(scores)
        averages.append(average)

    print("Average scores:", averages)
