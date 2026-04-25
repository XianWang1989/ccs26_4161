
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate the birth date
    valid_date = True
    month = int(month)
    day = int(day)

    if month == 2:
        if day > 29 or (day == 29 and int(year) % 4 != 0):
            valid_date = False
    elif month in {1, 3, 5, 7, 8, 10, 12}:
        if day > 31:
            valid_date = False
    elif month in {4, 6, 9, 11}:
        if day > 30:
            valid_date = False
    else:
        valid_date = False

    if valid_date:
        break
    else:
        print("Please enter a valid date.")

# Assuming year input is valid, sum the digits of the year
year_sum = sum_digits(int(year))
print(f"The sum of the digits in your birth year is: {year_sum}")
