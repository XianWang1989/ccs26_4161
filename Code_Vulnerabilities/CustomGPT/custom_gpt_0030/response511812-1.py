
import string

def calculate_average(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    scores = []

    for line in lines:
        # Clean and split the line into components
        clean_line = line.strip()
        temp_array = clean_line.split(',')

        # Extract scores as integers
        scores_list = list(map(int, temp_array[1:]))  # Ignore the name and convert scores to integers
        scores.append(scores_list)

    # Calculate averages for each list of scores
    averages = [sum(score) / len(score) for score in scores]

    return averages

def main():
    filename = "Class1.txt"
    averages = calculate_average(filename)

    print("Average scores for each class:")
    for i, avg in enumerate(averages, start=1):
        print(f"Class {i}: {avg:.2f}")

if __name__ == "__main__":
    main()
