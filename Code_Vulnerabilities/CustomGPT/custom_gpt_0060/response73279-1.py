
def sum_of_digits(n):
    while n >= 10:  # Continue until n is less than 10
        n = sum(int(digit) for digit in str(n))
    return n

# Date Input
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate the birth date
    if (int(month) == 2 and int(day) <= 29) or \
       (int(month) in {1, 3, 5, 7, 8, 10, 12} and int(day) <= 31) or \
       (int(month) in {4, 6, 9, 11} and int(day) <= 30):
        break  # Valid date, exit the loop
    else:
        print("Please enter a valid input")

# Calculate the sum of the digits of the year
sumYear = sum(int(digit) for digit in year)  # Sum digits of the year
result = sum_of_digits(sumYear)  # Reduce sumYear if >= 10

print(f"The final sum of the digits in your birth year is: {result}")
