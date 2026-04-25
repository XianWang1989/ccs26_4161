
def sum_digits(n):
    total = 0
    while n >= 10:
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total
    return total

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if int(month) == 2 and int(day) <= 29:  # Leap year handling not included for simplicity
        break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
        break
    elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
        break
    else:
        print("Please enter a valid input")

# Example usage of summing the digits of the year
sumYear = sum_digits(int(year))
print("Sum of the digits in the year:", sumYear)
