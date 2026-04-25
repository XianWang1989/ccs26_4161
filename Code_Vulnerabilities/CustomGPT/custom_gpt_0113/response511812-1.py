
import string

def calculate_averages(filename):
    with open(filename, "r") as file:
        # Read lines from the file
        lines = file.readlines()

    results = []

    # Process each line
    for line in lines:
        # Clean and split the line
        cleaned_line = line.strip()
        temp_array = cleaned_line.split(',')

        # Extracting the scores as integers
        scores = [int(score) for score in temp_array[1:]]  # Convert scores to integers
        results.append(scores)

    return results

def calculate_average(scores_list):
    # Calculate the average of each list of scores
    averages = []
    for scores in scores_list:
        avg = sum(scores) / len(scores) if scores else 0
        averages.append(avg)
    return averages

# Main program
filename = "Class1.txt"
scores_list = calculate_averages(filename)
averages = calculate_average(scores_list)

# Print averages
for index, average in enumerate(averages):
    print(f"Class {index + 1} average score: {average}")
