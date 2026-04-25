
def calculate_average(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_scores = []

    for line in lines:
        # Clean and split the line
        parts = line.strip().split(',')
        # Extract scores and convert to integers
        scores = list(map(int, parts[1:]))
        total_scores.append(scores)

    # Calculate averages for each class
    averages = []

    for scores in total_scores:
        average = sum(scores) / len(scores)
        averages.append(average)

    return averages

# Specify the file path
file_path = "Class1.txt"
averages = calculate_average(file_path)
print("Average scores:", averages)
