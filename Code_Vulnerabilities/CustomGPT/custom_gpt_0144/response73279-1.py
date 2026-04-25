def sum_digits(num):
    """Sums the digits of a number until the sum is less than 10."""
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

# Input loop for birth date validation
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate month and day
    try:
        month = int(month)
        day = int(day)
        year = int(year)

        if (month == 2 and day <= 29):  # February handling
            break
        elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:  # Months with 31 days
            break
        elif month in [4, 6, 9, 11] and day <= 30:  # Months with 30 days
            break
        else:
            print("Please enter a valid input.")
    except ValueError:
        print("Please enter a valid number for year, month, and day.")

# Sum the digits of year, month, and day
sumYear = sum_digits(year)
sumMonth = sum_digits(month)
sumDay = sum_digits(day)

print(f"Sum of year digits: {sumYear}")
print(f"Sum of month digits: {sumMonth}")
print(f"Sum of day digits: {sumDay}")
