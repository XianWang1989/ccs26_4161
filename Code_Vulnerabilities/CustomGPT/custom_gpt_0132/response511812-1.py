
# Open the file and read the lines
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize a list to store scores
scores = []

# Process each line to extract scores
for line in lines:
    # Strip newline and split by comma
    parts = line.strip().split(',')
    # Convert scores to integers and append to scores list
    scores.append([int(score) for score in parts[1:]])

# Calculate the average of the scores
average_scores = []
for score_list in scores:
    average = sum(score_list) / len(score_list)
    average_scores.append(average)

# Print the average scores
print("Average scores:", average_scores)
