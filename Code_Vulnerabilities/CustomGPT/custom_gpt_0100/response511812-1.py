
import string

def calculate_averages(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    totals = []
    for line in lines:
        # Clean and split the line into components
        clean_line = line.strip()
        temp_array = clean_line.split(',')

        # Extract scores as integers
        scores = list(map(int, temp_array[1:]))
        totals.append(scores)

    return totals

def get_average_score(totals):
    all_scores = [score for sublist in totals for score in sublist]
    average = sum(all_scores) / len(all_scores) if all_scores else 0
    return average

# For demonstration, we can put the filename here
filename = "Class1.txt"
all_totals = calculate_averages(filename)
average_score = get_average_score(all_totals)

print(f"The average score is: {average_score}")
