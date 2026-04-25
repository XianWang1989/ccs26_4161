
def validate_date(year, month, day):
    # Check for valid month and day
    if int(month) == 2:
        return int(day) <= 29  # Allow leap years as well
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
        return int(day) <= 31
    elif int(month) in [4, 6, 9, 11]:
        return int(day) <= 30
    return False

def digit_sum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

# Main loop
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if validate_date(year, month, day):
        break
    else:
        print("Please enter a valid input")

# Calculate the digit sum of the year
sum_year = digit_sum(year)

# Repeat the digit sum process while the sum is greater than or equal to 10
while sum_year >= 10:
    sum_year = digit_sum(sum_year)

print(f"The final sum of the digits in the year {year} is: {sum_year}")
