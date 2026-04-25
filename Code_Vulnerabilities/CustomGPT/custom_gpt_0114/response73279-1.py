
def sum_of_digits(value):
    while value >= 10:
        value = sum(int(digit) for digit in str(value))
    return value

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    month = int(month)
    day = int(day)

    if (month == 2 and day <= 29) or \
       (month in {1, 3, 5, 7, 8, 10, 12} and day <= 31) or \
       (month in {4, 6, 9, 11} and day <= 30):
        break
    else:
        print("Please enter a valid input.")

# Summing up the individual digits of the birth year
sum_year = sum_of_digits(int(year))
print("Final digit sum of your birth year:", sum_year)
