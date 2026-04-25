
def is_valid_date(month, day):
    if month == 2:
        return day <= 29  # Leap year check can be added if necessary
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return day <= 31
    elif month in [4, 6, 9, 11]:
        return day <= 30
    return False

# Function to sum the digits until they are less than 10
def sum_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

while True:
    year = input("Please enter the year you were born: ")
    month = int(input("Please enter the month you were born: "))
    day = int(input("Please enter the day you were born: "))

    if is_valid_date(month, day):
        break
    else:
        print("Please enter a valid input")

# Example usage with your sumYear
sumYear = sum_digits(int(year))
print("The reduced sum of your birth year is:", sumYear)
