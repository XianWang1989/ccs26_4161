
def digit_sum(n):
    total = 0
    while n >= 10:  # Continue until the sum is a single digit
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total
    return total

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate month and day
    valid_date = False
    month = int(month)
    day = int(day)

    if month == 2 and day <= 29:
        valid_date = True
    elif month in {1, 3, 5, 7, 8, 10, 12} and day <= 31:
        valid_date = True
    elif month in {4, 6, 9, 11} and day <= 30:
        valid_date = True

    if valid_date:
        sumYear = digit_sum(int(year))  # Calculate digit sum of the year
        print(f"The digit sum of the year is: {sumYear}")
        break
    else:
        print("Please enter a valid input")
