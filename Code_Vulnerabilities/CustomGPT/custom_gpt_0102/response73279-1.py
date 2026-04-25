
def sum_of_digits(n):
    """Function to sum the digits of a number, repeating if >= 10."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born (01-12): ")
    day = input("Please enter the day you were born (01-31): ")

    month = int(month)
    day = int(day)

    # Validate date
    if (month == 2 and day <= 29) or \
       (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or \
       (month in [4, 6, 9, 11] and day <= 30):
        break
    else:
        print("Please enter a valid date.")

# Sum the digits of the year
sumYear = sum(int(d) for d in year)
result = sum_of_digits(sumYear)

print(f"The final sum of the digits of your birth year is: {result}")
