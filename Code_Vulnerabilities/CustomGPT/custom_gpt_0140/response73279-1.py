
def sum_digits(n):
    """Sum the digits of a number."""
    total = 0
    while n >= 10:  # Keep summing until it's a single digit
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
    if int(month) == 2 and int(day) <= 29:
        break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
        break
    elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
        break
    else:
        print("Please enter a valid input")

# Convert year to int and sum its digits
sum_year = sum_digits(int(year))
print(f"The sum of the digits of your birth year is: {sum_year}")
