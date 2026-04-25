
def digit_sum(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born (01-12): ")
    day = input("Please enter the day you were born (01-31): ")

    month, day = int(month), int(day)

    if month == 2 and day <= 29:
        break
    elif month in {1, 3, 5, 7, 8, 10, 12} and day <= 31:
        break
    elif month in {4, 6, 9, 11} and day <= 30:
        break
    else:
        print("Please enter a valid input.")

# Calculate the digit sum for the year
sumYear = digit_sum(int(year))
print("Final sum of the year digits:", sumYear)
