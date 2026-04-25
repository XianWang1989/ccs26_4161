
def sum_digits(number):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number

def is_valid_date(month, day):
    if month == 2:
        return day <= 29  # Adjust if you want to consider leap years
    elif month in {1, 3, 5, 7, 8, 10, 12}:
        return day <= 31
    elif month in {4, 6, 9, 11}:
        return day <= 30
    return False

while True:
    year = input("Please enter the year you were born: ")
    month = int(input("Please enter the month you were born: "))
    day = int(input("Please enter the day you were born: "))

    if is_valid_date(month, day):
        break
    else:
        print("Please enter a valid input")

# Sum the digits of the year
sum_year = sum_digits(int(year))
print(f"The sum of the digits in the year {year} is: {sum_year}")
