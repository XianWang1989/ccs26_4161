
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    try:
        month = int(month)
        day = int(day)

        if (month == 2 and day <= 29) or \
           (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or \
           (month in [4, 6, 9, 11] and day <= 30):
            break
        else:
            print("Please enter a valid input")
    except ValueError:
        print("Please enter numerical values only")

# Example usage of digit_sum
sumYear = digit_sum(int(year))
print(f"The digit sum of your birth year is: {sumYear}")
