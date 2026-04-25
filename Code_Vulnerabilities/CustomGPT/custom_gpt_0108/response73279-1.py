
def digit_sum(n):
    """Calculate the sum of digits recursively until the sum is less than 10."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Ensure the inputs are valid
    if int(month) == 2 and int(day) <= 29:  # February
        break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:  # Months with 31 days
        break
    elif int(month) in [4, 6, 9, 11] and int(day) <= 30:  # Months with 30 days
        break
    else:
        print("Please enter a valid input")

# Perform digit sum
sumYear = digit_sum(int(year))
print(f"The digit sum of your birth year is: {sumYear}")
