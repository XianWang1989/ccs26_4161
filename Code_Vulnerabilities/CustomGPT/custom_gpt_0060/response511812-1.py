
import string

def calculate_average(file_path):
    # Open the file and read lines
    with open(file_path, "r") as file:
        lines = file.readlines()

    averages = []

    # Process each line in the file
    for line in lines:
        # Remove any trailing newline characters and split by comma
        new_line = line.strip()
        tempArray = new_line.split(',')

        # Remove the name (first element) and convert scores to integers
        scores = list(map(int, tempArray[1:]))

        # Calculate average if there are scores
        if scores:
            average = sum(scores) / len(scores)
            averages.append((tempArray[0], average))  # Append (name, average)

    return averages


# Call function and print result
file_path = "Class1.txt"  # Update this to your actual file path
averages = calculate_average(file_path)

for student, avg in averages:
    print(f"{student}: Average Score = {avg:.2f}")
