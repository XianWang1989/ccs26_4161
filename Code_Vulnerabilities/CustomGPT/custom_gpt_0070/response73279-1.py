
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Input and validation loop for birth date
while True:
    year = int(input("Please enter the year you were born: "))
    month = int(input("Please enter the month you were born: "))
    day = int(input("Please enter the day you were born: "))

    # Validate month and day
    if month == 2:  # February
        if day < 1 or day > 29:  # Leap year consideration can be added
            print("Please enter a valid date for February.")
            continue
    elif month in [1, 3, 5, 7, 8, 10, 12]:  # Months with 31 days
        if day < 1 or day > 31:
            print("Please enter a valid date for this month.")
            continue
    elif month in [4, 6, 9, 11]:  # Months with 30 days
        if day < 1 or day > 30:
            print("Please enter a valid date for this month.")
            continue
    else:
        print("Please enter a valid month.")
        continue

    break  # Exit the loop if input is valid

# Calculate digit sum of the year
result = digit_sum(year)
print(f"The single-digit sum of your birth year is: {result}")
