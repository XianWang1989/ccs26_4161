
def calculate_average_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    scores = []

    for line in lines:
        # Split the line and convert scores to integers
        data = line.strip().split(',')
        # Append the scores from each line to the scores list
        scores.append(list(map(int, data[1:])))  # Exclude the name

    # Calculate the average for each class
    averages = [sum(score_list) / len(score_list) for score_list in zip(*scores)]

    return averages

# Specify the file name
filename = "Class1.txt"
average_scores = calculate_average_from_file(filename)

print("Average scores for each class:", average_scores)
