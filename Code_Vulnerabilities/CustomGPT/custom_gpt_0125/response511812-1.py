
import string

def calculate_average(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()

    all_scores = []

    for line in lines:
        stripped_line = string.strip(line, '\n')
        temp_array = stripped_line.split(',')
        # Extract scores from the line and convert to int
        scores = list(map(int, temp_array[1:]))
        all_scores.append(scores)

    averages = [sum(scores) / len(scores) for scores in all_scores]
    return averages

# Usage
averages = calculate_average("Class1.txt")
print("Average scores: ", averages)
