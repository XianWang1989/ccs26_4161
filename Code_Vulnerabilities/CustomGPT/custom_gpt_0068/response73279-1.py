
def sum_digits(number):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number

# Loop for user input until a valid date is entered
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Check for valid dates
    if int(month) == 2:
        if int(day) <= 29:  # Note: No need to check for leap years for simplicity
            break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) <= 31:
            break
    elif int(month) in [4, 6, 9, 11]:
        if int(day) <= 30:
            break
    else:
        print("Please enter a valid date.")

# Example: summing digits of the year input
sumYear = sum_digits(int(year))
print(f"The single-digit sum of your birth year is: {sumYear}")
