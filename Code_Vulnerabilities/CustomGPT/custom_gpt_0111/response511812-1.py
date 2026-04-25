
def calculate_average(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

    total_scores = []
    for line in lines:
        # Strip newline and split by comma
        parts = line.strip().split(',')
        # Convert score strings to integers and append to total_scores
        scores = list(map(int, parts[1:]))  # Skip the name (first part)
        total_scores.append(scores)

    # Calculate the average for each student
    averages = []
    for scores in total_scores:
        average = sum(scores) / len(scores)
        averages.append(average)

    return averages

# Use the function
file_name = "Class1.txt"
averages = calculate_average(file_name)
print("Averages:", averages)
