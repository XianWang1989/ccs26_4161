
def sum_digits(n):
    total = 0
    while n >= 10:
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    month = int(month)
    day = int(day)

    if (month == 2 and day <= 29) or (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or (month in [4, 6, 9, 11] and day <= 30):
        break
    else:
        print("Please enter a valid date.")

# Example for summing the year
sumYear = sum_digits(int(year))
print("Sum of digits in birth year:", sumYear)
