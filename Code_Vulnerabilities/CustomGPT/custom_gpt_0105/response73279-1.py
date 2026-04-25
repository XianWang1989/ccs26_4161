
def validate_date(year, month, day):
    if month == 2 and day <= 29:
        return True
    elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
        return True
    elif month in [4, 6, 9, 11] and day <= 30:
        return True
    return False

def sum_digits(num):
    total = 0
    while num >= 10:
        total = 0
        for digit in str(num):
            total += int(digit)
        num = total
    return total

while True:
    year = int(input("Please enter the year you were born: "))
    month = int(input("Please enter the month you were born: "))
    day = int(input("Please enter the day you were born: "))

    if validate_date(month, day):
        break
    else:
        print("Please enter a valid input.")

# Sum the digits of the year now
final_sum = sum_digits(year)
print("The sum of the digits in the year is:", final_sum)
