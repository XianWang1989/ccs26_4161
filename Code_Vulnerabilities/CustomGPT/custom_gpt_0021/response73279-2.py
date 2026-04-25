
def sum_digits(number):
    total = sum(int(digit) for digit in str(number))
    return total

while True:
    year = int(input("Please enter the year you were born: "))
    month = int(input("Please enter the month you were born: "))
    day = int(input("Please enter the day you were born: "))

    # Check date validity
    if (month == 2 and day <= 29) or \
       (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or \
       (month in [4, 6, 9, 11] and day <= 30):
        break
    else:
        print("Please enter a valid input")

# Now sum the digits of the year, month, and day
total_sum = year + month + day
while total_sum >= 10:
    total_sum = sum_digits(total_sum)

print("Final sum of the digits is:", total_sum)
