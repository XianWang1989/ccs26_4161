
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))  # Using a generator expression instead of sum()
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Convert month and day to integers
    month = int(month)
    day = int(day)

    if month == 2 and day <= 29:  # Input validation for February
        break
    elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:  # Input validation for 31-day months
        break
    elif month in [4, 6, 9, 11] and day <= 30:  # Input validation for 30-day months
        break
    else:
        print("Please enter a valid input")

# Now sum the digits of the birth year
sum_year = sum_digits(int(year))
print(f"The final digit sum of your birth year is: {sum_year}")
