
import string

def calculate_average(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    averages = []

    for line in lines:
        # Strip whitespace and split the line into components
        components = line.strip().split(',')
        name = components[0]  # Name of the student
        scores = list(map(int, components[1:]))  # Convert score strings to integers

        # Calculate the average score
        if scores:
            average_score = sum(scores) / len(scores)
            averages.append((name, average_score))

    return averages

# Path to your file
file_path = "Class1.txt"
average_scores = calculate_average(file_path)

# Display the results
for name, avg in average_scores:
    print(f"{name}: {avg:.2f}")
