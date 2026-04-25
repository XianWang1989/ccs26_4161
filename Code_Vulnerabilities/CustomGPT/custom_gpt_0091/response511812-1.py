
import string

# Function to calculate the average scores
def calculate_average(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

    scores = []

    for line in lines:
        # Strip newline and split the line into parts
        parts = string.strip(line, '\n').split(',')
        # Extract scores and convert to integers
        try:
            scores_list = [int(part) for part in parts[1:]]
            scores.append(scores_list)
        except ValueError:
            print(f"Invalid data in line: {line}")

    if scores:
        # Calculate averages for each student
        averages = [sum(score) / len(score) for score in scores]
        return averages
    else:
        return []

# Get the averages from the text file
averages = calculate_average("Class1.txt")
print("Average scores for each student:", averages)
