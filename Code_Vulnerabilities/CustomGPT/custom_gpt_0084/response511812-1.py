
import string

def calculate_average(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    total_scores = []
    for line in lines:
        # Remove newline and split by comma
        line = line.strip()
        temp_array = line.split(',')

        # Convert scores to integers and store in a list
        scores = list(map(int, temp_array[1:]))  # Skip the name part
        total_scores.append(scores)

    # Calculate average for each student
    averages = []
    for scores in total_scores:
        average = sum(scores) / len(scores)
        averages.append(average)

    return averages

# Usage
averages = calculate_average("Class1.txt")
print("Average scores:", averages)
