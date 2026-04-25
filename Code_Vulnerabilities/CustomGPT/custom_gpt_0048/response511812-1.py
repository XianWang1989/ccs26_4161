
# Open the file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize variables to store the scores
scores_list = []

# Process each line
for line in lines:
    # Clean and split the line into components
    tempArray = line.strip().split(',')

    # Extract scores as integers
    scores = list(map(int, tempArray[1:]))  # Convert scores to integers
    scores_list.append(scores)

# Calculate averages
if scores_list:  # Ensure there are scores to calculate
    average_scores = [sum(scores) / len(scores) for scores in scores_list]
    overall_average = sum(average_scores) / len(average_scores)

    print("Average scores for each student:", average_scores)
    print("Overall average score:", overall_average)
