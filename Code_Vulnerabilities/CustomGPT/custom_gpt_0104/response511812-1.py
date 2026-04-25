
# Open the file
file = open("Class1.txt", "r")

# Initialize a variable for the total score and a counter
total_scores = []
number_of_students = 0

# Read each line from the file and process it
for line in file:
    # Remove any trailing newline characters
    new_line = line.strip()
    # Split the line by commas
    tempArray = new_line.split(',')

    # Extracts scores and converts them to integers
    scores = list(map(int, tempArray[1:]))  # Extract scores and convert to integers
    total_scores.extend(scores)  # Append to total scores list
    number_of_students += 1       # Count the students

# Calculate the average if there are scores
if total_scores:
    average = sum(total_scores) / len(total_scores)  # Only takes into account the scores
else:
    average = 0

# Print out the average
print("Average score:", average)

# Don't forget to close the file
file.close()
