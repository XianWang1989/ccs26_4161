
import string

def calculate_average(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    scores = []

    for line in lines:
        # Remove newline and split the line by commas
        data = line.strip().split(',')
        # Convert scores to integers
        student_scores = list(map(int, data[1:]))
        # Append to scores list
        scores.append(student_scores)

    # Calculate average for each student
    averages = []
    for student in scores:
        average = sum(student) / len(student)
        averages.append(average)

    return averages

# Example usage
file_path = "Class1.txt"  # Replace with your actual file path
average_scores = calculate_average(file_path)
print("Average Scores:", average_scores)
