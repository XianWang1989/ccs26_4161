
def is_valid_date(year, month, day):
    """Check if the provided date is valid."""
    if int(month) == 2:
        return 1 <= int(day) <= 29  # February has either 28 or 29 days.
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= int(day) <= 31  # These months have 31 days.
    elif int(month) in [4, 6, 9, 11]:
        return 1 <= int(day) <= 30  # These months have 30 days.
    return False

def sum_digits(n):
    """Sum the digits of a number until the sum is < 10."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Main loop to get valid birthday input
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if is_valid_date(year, month, day):
        break
    else:
        print("Please enter a valid input.")

# Calculate the sum of the digits of the year
sumYear = sum(int(digit) for digit in year)

# Conditionally sum digits of the year until the sum is < 10
final_sum = sum_digits(sumYear)

print("The final sum of the digits is:", final_sum)
