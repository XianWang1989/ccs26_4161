
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    valid_date = False
    month = int(month)
    day = int(day)

    if month == 2 and day <= 29:
        valid_date = True
    elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
        valid_date = True
    elif month in [4, 6, 9, 11] and day <= 30:
        valid_date = True

    if valid_date:
        break
    else:
        print("Please enter a valid input.")

# Now sum up the digits of the year
sum_year = digit_sum(int(year))
print(f"The reduced year sum is: {sum_year}")
