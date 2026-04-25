
# Open the file containing the scores
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize a list to store averages
averages = []

# Loop through each line in the file
for line in lines:
    # Strip whitespace and newline characters, then split the line into parts
    parts = line.strip().split(',')

    # Extract the name and convert scores to integers
    name = parts[0]
    scores = list(map(int, parts[1:]))  # Convert the score strings to integers

    # Calculate the average of the scores
    average = sum(scores) / len(scores)  # Calculate average

    # Store the average in a dictionary
    averages.append((name, average))  # Store as tuple (name, average)

# Print the averages
for name, average in averages:
    print(f"{name}'s average score is: {average:.2f}")
