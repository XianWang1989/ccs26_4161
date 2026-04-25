
# Open the file and read the contents
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize a list to hold all scores
all_scores = []

# Process each line in the file
for line in lines:
    # Strip any whitespace and newline characters from the ends
    cleaned_line = line.strip()
    # Split the line into components (name and scores)
    parts = cleaned_line.split(',')

    # Ensure there are at least 2 scores in each line
    if len(parts) >= 2:
        # Convert the score strings to integers and add to all_scores
        scores = [int(score) for score in parts[1:]]
        all_scores.append(scores)

# Initialize a variable to hold total scores and count
total_scores = []
count = 0

# Calculate the average for each list of scores
for scores in all_scores:
    count += len(scores)  # Update the total count of scores
    total_scores.append(sum(scores))  # Sum the scores for the current line

# Calculate the average score
if count > 0:
    average = sum(total_scores) / len(total_scores)  # Average of all scores
    print(f'Average score: {average}')
else:
    print('No scores to average.')
