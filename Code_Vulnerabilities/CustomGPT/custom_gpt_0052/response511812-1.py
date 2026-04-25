
# Define function to calculate average scores
def calculate_average(filename):
    total_scores = []

    with open(filename, "r") as file:
        lines = file.readlines()

        for line in lines:
            # Strip newline and split by comma
            parts = line.strip().split(',')
            # Convert score strings to integers and append to total_scores
            scores = list(map(int, parts[1:]))  # Skip the name and convert scores to int
            total_scores.append(scores)

    # Calculate average for each class
    averages = []
    for scores in total_scores:
        average = sum(scores) / len(scores)
        averages.append(average)

    return averages

# Example usage
filename = "Class1.txt"
averages = calculate_average(filename)
print("Average scores for each class:", averages)
