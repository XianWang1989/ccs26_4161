
def sum_of_digits(n):
    """Function to sum the digits of a number."""
    total = 0
    while n >= 10:
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate the date input
    if int(month) == 2 and int(day) <= 29:  # Leap year not checked
        break
    elif int(month) in {1, 3, 5, 7, 8, 10, 12} and int(day) <= 31:
        break
    elif int(month) in {4, 6, 9, 11} and int(day) <= 30:
        break
    else:
        print("Please enter a valid date.")

# Calculate the sum of digits for year
sum_year = sum_of_digits(int(year))
print(f"The sum of the digits in the year {year} is: {sum_year}")
