
def sum_of_digits(n):
    # Function to sum the digits of n until a single digit is reached
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate month and day
    if int(month) == 2:
        if int(day) <= 29:  # Checks for leap year as well, not implemented in this simple validation
            break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) <= 31:
            break
    elif int(month) in [4, 6, 9, 11]:
        if int(day) <= 30:
            break
    else:
        print("Please enter a valid input")

# Calculate the sum of the digits of the year
year_sum = sum_of_digits(int(year))
print(f"The sum of the digits in your year of birth is: {year_sum}")
