
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born (01-12): ")
    day = input("Please enter the day you were born (01-31): ")

    month = int(month)
    day = int(day)

    if (month == 2 and day <= 29) or \
       (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or \
       (month in [4, 6, 9, 11] and day <= 30):
        break
    else:
        print("Please enter a valid input.")

# Now we calculate the sum of the digits of the year
sumYear = digit_sum(int(year))
print("Final digit sum of the year:", sumYear)
