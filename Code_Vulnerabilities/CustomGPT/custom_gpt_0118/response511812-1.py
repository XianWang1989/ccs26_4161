
import string

# Function to calculate average scores from a file
def calculate_averages(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    averages = []

    for line in lines:
        # Clean the line and split into parts
        new_line = line.strip()  # Remove newline characters
        temp_array = new_line.split(',')

        # Get the scores as integers
        scores = list(map(int, temp_array[1:]))  # Convert scores to integers
        average_score = sum(scores) / len(scores)  # Calculate average
        averages.append((temp_array[0], average_score))  # Append name and average

    return averages

# Usage
averages = calculate_averages("Class1.txt")
for name, average in averages:
    print(f"{name}: {average:.2f}")
