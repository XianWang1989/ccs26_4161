
def sum_digits(n):
    # Function to sum digits of a number until it's less than 10
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Check if the input dates are valid
    if int(month) == 2 and int(day) <= 29:  # Leap year not checked for simplicity
        break
    elif int(month) in {1, 3, 5, 7, 8, 10, 12} and int(day) <= 31:
        break
    elif int(month) in {4, 6, 9, 11} and int(day) <= 30:
        break
    else:
        print("Please enter a valid input")

# Sum the digits of the year and repeat if necessary
year_sum = sum_digits(int(year))
print(f"The sum of the digits in your birth year {year} is: {year_sum}")
