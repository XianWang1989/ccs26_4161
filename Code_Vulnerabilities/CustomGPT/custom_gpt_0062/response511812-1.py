
def calculate_average_from_file(file_path):
    options = ("alphabetical order", "highest to lowest", "average score")
    option = input("Which order do you want to output? " + str(options) + ": ")

    with open(file_path, "r") as file:
        lines = file.readlines()

    scores = []
    for line in lines:
        parts = line.strip().split(',')
        name = parts[0]
        # Convert the remaining parts to integers
        scores.append([name] + list(map(int, parts[1:])))

    # Calculate average scores
    if option == "average score":
        total_scores = [sum(student[1:]) for student in scores]
        averages = [total / len(student[1:]) for student, total in zip(scores, total_scores)]

        for student, avg in zip(scores, averages):
            print(f"{student[0]}: Average score = {avg:.2f}")

# Example usage
calculate_average_from_file("Class1.txt")
