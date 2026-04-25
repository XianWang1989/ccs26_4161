
def sum_digits(num):
    """Function to sum digits of a number, repeating if >= 10."""
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate month and day
    month = int(month)
    day = int(day)

    if month == 2 and day <= 29:  # Allow 29 for leap years as well
        break
    elif month in {1, 3, 5, 7, 8, 10, 12} and day <= 31:
        break
    elif month in {4, 6, 9, 11} and day <= 30:
        break
    else:
        print("Please enter a valid input")

# Calculate and sum the digits of the year
sum_year = sum(int(digit) for digit in year)
final_sum = sum_digits(sum_year)

print(f"The final sum of digits in the year is: {final_sum}")
