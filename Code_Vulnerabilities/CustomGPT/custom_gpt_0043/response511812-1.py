
import string

# Define your options
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? (" + ", ".join(options) + "): ")

# Read data from file
file_path = "Class1.txt"
file = open(file_path, "r")

# Initialize a list to store all scores
all_scores = []

try:
    lines = file.readlines()
    for line in lines:
        # Strip line of newline characters and split by comma
        temp_array = line.strip().split(',')

        # Convert score strings to integers and store them in a list
        scores = list(map(int, temp_array[1:]))  # Skip the name
        all_scores.append(scores)

        # Print the printedArray from earlier, if needed
        print(f"Scores for {temp_array[0]}: {scores}")

    # Option for computing average scores
    if option == "average score":
        # Calculate the average for each class and overall
        score_totals = [sum(scores) for scores in all_scores]
        averages = [total / len(scores) for total, scores in zip(score_totals, all_scores)]

        for i, avg in enumerate(averages):
            print(f"Average score for Class {i + 1}: {avg:.2f}")

finally:
    file.close()
