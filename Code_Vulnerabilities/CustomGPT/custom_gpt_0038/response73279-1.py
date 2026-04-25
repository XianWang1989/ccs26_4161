
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate the month and day
    if (int(month) == 2 and int(day) <= 29) or \
       (int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31) or \
       (int(month) in [4, 6, 9, 11] and int(day) <= 30):
        break
    else:
        print("Please enter a valid input.")

# Sum the digits of the year
sumYear = sum(int(digit) for digit in year)

# Keep summing the digits until the result is a single digit
while sumYear >= 10:
    sumYear = sum(int(digit) for digit in str(sumYear))

print(f"The final sum of the digits in the year is: {sumYear}")
