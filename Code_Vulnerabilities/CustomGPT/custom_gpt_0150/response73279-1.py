
def sum_digits(number):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate month and day
    valid_date = True
    if int(month) == 2 and int(day) <= 29:
        if int(day) == 29 and int(year) % 4 != 0:  # Check for leap year
            valid_date = False
    elif int(month) in {1, 3, 5, 7, 8, 10, 12} and int(day) > 31:
        valid_date = False
    elif int(month) in {4, 6, 9, 11} and int(day) > 30:
        valid_date = False

    if valid_date:
        break
    else:
        print("Please enter a valid input.")

# Calculate the sum of the digits of the year
sumYear = sum_digits(int(year))
print(f"The reduced sum of your birth year digits is: {sumYear}")
