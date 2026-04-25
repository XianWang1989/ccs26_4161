
def sum_digits(n):
    while n >= 10:  # Repeat until the sum is a single digit
        n = sum(int(digit) for digit in str(n))  # Sum the digits
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Check if input dates are valid
    month = int(month)
    day = int(day)

    if (month == 2 and day <= 29) or \
       (month in {1, 3, 5, 7, 8, 10, 12} and day <= 31) or \
       (month in {4, 6, 9, 11} and day <= 30):
        break
    else:
        print("Please enter a valid input")

# Now calculate the sum of the digits of the year
sumYear = sum_digits(int(year))
print(f"The sum of the digits of your birth year is: {sumYear}")
