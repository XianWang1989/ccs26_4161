
def calculate_average(filename):
    try:
        with open(filename, "r") as file:
            total_sum = 0
            count = 0

            for line in file:
                data = line.strip().split(',')

                # Extract scores and convert to integers
                scores = list(map(int, data[1:]))

                # Update total sum and count
                total_sum += sum(scores)
                count += len(scores)

            # Calculate average
            if count == 0:
                return None  # Avoid division by zero
            average = total_sum / count
            return average

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

filename = "Class1.txt"
average_score = calculate_average(filename)
print(f"The average score is: {average_score}")
