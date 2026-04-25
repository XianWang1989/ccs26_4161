
def sum_of_digits(n):
    # Sum the digits of n until it's less than 10
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Input for birth date
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate the input is numeric
    if year.isdigit() and month.isdigit() and day.isdigit():
        month = int(month)
        day = int(day)

        # Date validation for February (leap year consideration not included for simplicity)
        if month == 2 and day <= 29:
            break
        elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
            break
        elif month in [4, 6, 9, 11] and day <= 30:
            break
        else:
            print("Please enter a valid date.")
    else:
        print("Please enter numeric values.")

# Calculate the sum of the year
sumYear = sum(int(digit) for digit in year)

# Use the sum_of_digits function to get to a single digit
final_sum = sum_of_digits(sumYear)

print(f"The final sum of the digits of your birth year is: {final_sum}")
