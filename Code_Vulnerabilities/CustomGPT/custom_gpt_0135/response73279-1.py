
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate the date inputs
    valid_date = False
    month = int(month)
    day = int(day)

    if month == 2:
        if day <= 29:  # Assuming leap years are accounted elsewhere
            valid_date = True
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day <= 31:
            valid_date = True
    elif month in [4, 6, 9, 11]:
        if day <= 30:
            valid_date = True

    if valid_date:
        break
    else:
        print("Please enter a valid input")

# Sum the digits of the year
sumYear = int(year)
final_sum = sum_digits(sumYear)
print("The final sum of the digits in your birth year is:", final_sum)
