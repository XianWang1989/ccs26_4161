
def sum_digits(n):
    """Sum the digits of a number, repeatedly if the sum is 10 or more."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if int(month) == 2 and int(day) <= 29:
        break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
        break
    elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
        break
    else:
        print("Please enter a valid input")

# Now calculate the sum of digits of the year
birth_year = int(year)
result = sum_digits(birth_year)
print("The repeated sum of the digits of your birth year is:", result)
