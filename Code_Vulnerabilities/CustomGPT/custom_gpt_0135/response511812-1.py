
def calculate_average(filename):
    # Open the file and read lines
    with open(filename, "r") as file:
        lines = file.readlines()

    all_scores = []  # List to hold all scores

    # Process each line
    for line in lines:
        # Clean up the line and split it into components
        parts = line.strip().split(',')
        # Extract the scores (assuming they are always the last three parts)
        scores = [int(part) for part in parts[1:]]  # Convert scores to integers
        all_scores.append(scores)  # Append the scores to the main list

    # Calculate the average for each student
    averages = []
    for scores in all_scores:
        avg = sum(scores) / len(scores)  # Average calculation
        averages.append(avg)

    # Print the average scores
    for i, avg in enumerate(averages):
        print(f"Average score for student {i + 1}: {avg:.2f}")

# Call the function with the filename
calculate_average("Class1.txt")
