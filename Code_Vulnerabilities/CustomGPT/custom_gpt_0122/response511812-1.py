
def calculate_average_scores(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_scores = [0, 0, 0]
    count = len(lines)

    for line in lines:
        parts = line.strip().split(',')
        # Ensure we only process valid scores
        if len(parts) > 1:
            scores = list(map(int, parts[1:]))  # Convert scores to integers
            for i in range(len(scores)):
                total_scores[i] += scores[i]

    # Calculate averages
    averages = [total / count for total in total_scores]
    return averages

# Example usage
averages = calculate_average_scores("Class1.txt")
print("Averages:", averages)
