
def calculate_average(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    all_scores = []

    for line in lines:
        # Strip whitespace and split by comma
        temp_array = line.strip().split(',')

        # Convert scores from string to int and append to all_scores
        scores = [int(score) for score in temp_array[1:]]  # Exclude the name part
        all_scores.append(scores)

    if not all_scores:
        return 0  # Avoid division by zero if there are no scores

    # Calculate the average per student
    averages = [sum(scores) / len(scores) for scores in all_scores]

    return averages

# Example usage
file_path = "Class1.txt"  # Adjust file path as needed
averages = calculate_average(file_path)
print("Average Scores:", averages)
