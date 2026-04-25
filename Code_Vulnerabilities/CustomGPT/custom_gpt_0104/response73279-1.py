
# Function to sum the digits of a number until it's less than 10
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Loop to get a valid date from the user
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born (1-12): ")
    day = input("Please enter the day you were born (1-31): ")

    # Convert to integers for validation
    month = int(month)
    day = int(day)

    valid_date = False
    if month == 2 and day <= 29:  # Check for February
        valid_date = True
    elif month in {1, 3, 5, 7, 8, 10, 12} and day <= 31:  # Months with 31 days
        valid_date = True
    elif month in {4, 6, 9, 11} and day <= 30:  # Months with 30 days
        valid_date = True

    if valid_date:
        print(f"You entered a valid date: {month}/{day}/{year}")
        break  # Exit the loop if the date is valid
    else:
        print("Please enter a valid input")

# Example usage of digit_sum function
# Let's say you want to derive the digit sum of the year
year_digits_sum = digit_sum(int(year))
print(f"The digit sum of your birth year is: {year_digits_sum}")
