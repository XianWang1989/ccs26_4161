
def sum_of_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate the inputs.
    month = int(month)
    day = int(day)

    if (month == 2 and day <= 29) or \
       (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or \
       (month in [4, 6, 9, 11] and day <= 30):
        break
    else:
        print("Please enter a valid input.")

# Calculate and sum the digits in the birth year
sumYear = sum(int(digit) for digit in year)
sumYear = sum_of_digits(sumYear)

print(f"The summed value of your birth year digits is: {sumYear}")
