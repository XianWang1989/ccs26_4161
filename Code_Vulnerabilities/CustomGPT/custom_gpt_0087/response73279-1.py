
# Part 1: Digit Summation Loop
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage
year = int(input("Please enter the year you were born: "))
sumYear = sum_digits(year)
print(f"Summed year digits: {sumYear}")


# Part 2: Validating Birth Date
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    month = int(month)
    day = int(day)

    # Check for valid date
    if month == 2 and day <= 29:
        break
    elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
        break
    elif month in [4, 6, 9, 11] and day <= 30:
        break
    else:
        print("Please enter a valid input")

print(f"Your birth date is: {year}-{month:02d}-{day:02d}")
