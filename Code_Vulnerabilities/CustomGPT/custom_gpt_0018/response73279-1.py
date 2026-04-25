
# Sum digits of the year until the sum is less than 10
def sum_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

# Input loop for validating the birth date
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    try:
        month = int(month)
        day = int(day)

        # Validate date
        if month == 2:
            if day <= 29:  # You may want to include leap year check for full validation
                break
        elif month in {1, 3, 5, 7, 8, 10, 12}:
            if day <= 31:
                break
        elif month in {4, 6, 9, 11}:
            if day <= 30:
                break
        else:
            print("Please enter a valid input.")
    except ValueError:  # Handle non-integer inputs
        print("Please enter numeric values.")

# Call the function to sum digits of the year
sumYear = sum_digits(int(year))
print(f"The final sum of the digits of your birth year is: {sumYear}")
