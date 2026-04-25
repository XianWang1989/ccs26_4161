
import string

def calculate_average(file_path):
    options = ("alphabetical order", "highest to lowest", "average score")
    option = input("Which order do you want to output? " + str(options) + ": ")

    with open(file_path, "r") as file:
        lines = file.readlines()

    results = []

    # Parse each line
    for line in lines:
        line = line.strip()
        temp_array = line.split(',')

        # Collect the scores as integers
        scores = [int(score) for score in temp_array[1:]]  # Ignore name
        results.append(scores)

    # Calculate the average if chosen
    if option == "average score":
        total_scores = [score for sublist in results for score in sublist]  # Flatten list of lists
        average = sum(total_scores) / len(total_scores) if total_scores else 0
        print("Average score:", average)

# Call the function with the appropriate file path
calculate_average("Class1.txt")
