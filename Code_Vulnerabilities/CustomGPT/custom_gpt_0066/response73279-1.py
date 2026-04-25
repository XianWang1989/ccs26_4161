
def sum_of_digits(n):
    """Repeat summing digits until the result is a single digit."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    month = int(month)
    day = int(day)

    # Validating the date
    if month == 2 and day <= 29:
        break
    elif month in {1, 3, 5, 7, 8, 10, 12} and day <= 31:
        break
    elif month in {4, 6, 9, 11} and day <= 30:
        break
    else:
        print("Please enter a valid date.")

# Example usage of sum_of_digits
sumYear = int(year)  # Example input for summation
result = sum_of_digits(sumYear)

print(f"The reduced sum of the year {year} is: {result}")
