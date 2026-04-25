
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    month = int(month)
    day = int(day)

    # Validate the date
    if (month == 2 and day <= 29) or \
       (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or \
       (month in [4, 6, 9, 11] and day <= 30):
        break
    else:
        print("Please enter a valid input")

# Sum the digits of the year
sumYear = int(year)
result = sum_digits(sumYear)
print(f"The digit sum of your birth year is: {result}")
