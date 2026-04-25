
def sum_digits(num):
    total = sum(int(digit) for digit in str(num))
    return total

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate the date
    if int(month) == 2 and int(day) <= 29:
        break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
        break
    elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
        break
    else:
        print("Please enter a valid input")

# Calculate and sum the digits of the year
sumYear = sum_digits(int(year))

# Continue summing digits until the result is less than 10
while sumYear >= 10:
    sumYear = sum_digits(sumYear)

print("Final sum of digits:", sumYear)
