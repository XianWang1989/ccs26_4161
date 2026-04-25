
def get_birth_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        # Check for valid dates
        if int(month) == 2 and int(day) <= 29:
            break
        elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
            break
        elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
            break
        else:
            print("Please enter a valid input")

    return year, month, day

def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Get user input
year, month, day = get_birth_date()

# Sum digits of the year
sum_year = sum_digits(int(year))
print(f"Sum of digits in year: {sum_year}")

# Optionally, sum digits of month and day too
sum_month = sum_digits(int(month))
sum_day = sum_digits(int(day))

print(f"Sum of digits in month: {sum_month}")
print(f"Sum of digits in day: {sum_day}")
