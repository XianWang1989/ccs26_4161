
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def get_birth_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        month = int(month)
        day = int(day)

        if (month == 2 and day <= 29) or \
           (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or \
           (month in [4, 6, 9, 11] and day <= 30):
            break
        else:
            print("Please enter a valid input")

    return year, month, day

# Get user input
year, month, day = get_birth_date()

# Sum digits
year_sum = sum_digits(int(year))
month_sum = sum_digits(month)
day_sum = sum_digits(day)

print(f"Sum of digits for year: {year_sum}, month: {month_sum}, day: {day_sum}")
