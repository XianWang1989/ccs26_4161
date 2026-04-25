
def valid_date(month, day):
    if month == 2:
        return day <= 29  # Leap year not considered for simplicity
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return day <= 31
    elif month in [4, 6, 9, 11]:
        return day <= 30
    return False

def sum_digits(n):
    total = 0
    while n >= 10:  # Keep summing until n < 10
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    month_int = int(month)
    day_int = int(day)

    if valid_date(month_int, day_int):
        break
    else:
        print("Please enter a valid input")

# Calculate the sum of the digits of the year
sum_year = sum_digits(int(year))
print(f"The sum of the digits of your birth year is: {sum_year}")
