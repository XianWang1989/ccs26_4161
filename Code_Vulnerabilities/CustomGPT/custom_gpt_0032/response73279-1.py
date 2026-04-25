
# Function to calculate the digit sum until it's a single digit
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Input loop for birthdate validation
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born (1-12): ")
    day = input("Please enter the day you were born: ")

    # Convert inputs to integers for validation
    month = int(month)
    day = int(day)

    # Validate day based on month
    if month == 2 and day <= 29:  # February
        break
    elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:  # Months with 31 days
        break
    elif month in [4, 6, 9, 11] and day <= 30:  # Months with 30 days
        break
    else:
        print("Please enter a valid date.")

# Calculate the sum of digits for the year
sum_year = digit_sum(int(year))
print(f"The reduced sum of your birth year digits is: {sum_year}")
