
def sum_digits(n):
    total = n
    while total >= 10:
        total = sum(int(digit) for digit in str(total))
    return total

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    month, day = int(month), int(day)

    if (month == 2 and day <= 29) or \
       (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or \
       (month in [4, 6, 9, 11] and day <= 30):
        break
    else:
        print("Please enter a valid input")

# Summing the digits of the year
sumYear = sum_digits(int(year))
print(f"Sum of digits in the year: {sumYear}")
