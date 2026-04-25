
def calculate_average(file_path):
    # Read the file and extract data
    with open(file_path, 'r') as file:
        lines = file.readlines()

    averages = []

    for line in lines:
        data = line.strip().split(',')
        scores = list(map(int, data[1:]))  # Convert scores to integers
        average = sum(scores) / len(scores)  # Calculate average
        averages.append((data[0], average))  # Store name and average

    return averages

# Usage
file_path = "Class1.txt"
averages = calculate_average(file_path)

# Print the average scores
for name, avg in averages:
    print(f"{name}'s average score: {avg}")
