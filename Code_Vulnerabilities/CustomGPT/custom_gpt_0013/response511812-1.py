
# Function to calculate the average from the scores
def calculate_average(scores):
    return sum(scores) / len(scores)

# Read data from the file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize a list to store averages
averages = []

# Process each line in the file
for line in lines:
    # Strip any whitespace and split by comma
    tempArray = line.strip().split(',')

    # Extract the scores as integers
    scores = list(map(int, tempArray[1:]))  # Convert scores to integers

    # Calculate the average and append to the list
    avg = calculate_average(scores)
    averages.append((tempArray[0], avg))  # Store name and average

# Print the averages for each student
for name, avg in averages:
    print(f"{name}: Average Score = {avg:.2f}")

# If you want to calculate the overall average score
overall_average = calculate_average([avg for _, avg in averages])
print(f"Overall Average Score = {overall_average:.2f}")
