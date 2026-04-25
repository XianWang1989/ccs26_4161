
def digit_sum(n):
    """Calculate the sum of the digits of a number."""
    total = 0
    while n >= 10:
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total
    return n

def is_valid_date(month, day, year):
    """Check if the provided date is valid."""
    if month == 2:
        # Check for leap year
        return day <= (29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28)
    elif month in [4, 6, 9, 11]:
        return day <= 30
    else:
        return day <= 31

while True:
    year = int(input("Please enter the year you were born: "))
    month = int(input("Please enter the month you were born (1-12): "))
    day = int(input("Please enter the day you were born: "))

    if is_valid_date(month, day, year):
        break
    else:
        print("Please enter a valid input")

# Sum the digits of the year
year_sum = digit_sum(year)

# If the digit sum is < 10, output it
print(f"The digit sum of your birth year is: {year_sum}")
