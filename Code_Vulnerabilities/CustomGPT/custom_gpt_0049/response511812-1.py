
import string

# Function to calculate the average score from the given data
def calculate_average(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    scores = []

    # Process each line to extract scores
    for line in lines:
        new_line = line.strip()
        if new_line:  # Check if the line is not empty
            temp_array = new_line.split(',')
            # Extract the scores as integers
            scores.append(list(map(int, temp_array[1:])))

    # Calculate the average for each student's scores
    if scores:
        average_scores = [sum(score) / len(score) for score in scores]
        return average_scores
    else:
        return []

# Entry point
filename = "Class1.txt"
averages = calculate_average(filename)
print("Average scores for each student:", averages)
