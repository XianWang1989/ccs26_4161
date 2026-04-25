
def get_valid_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        # Validate month and day
        if int(month) == 2 and int(day) <= 29:  # February
            break
        elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:  # 31-day months
            break
        elif int(month) in [4, 6, 9, 11] and int(day) <= 30:  # 30-day months
            break
        else:
            print("Please enter a valid input")

    return int(year), int(month), int(day)

def digit_sum(value):
    while value >= 10:
        value = sum(int(digit) for digit in str(value))
    return value

# Get valid birth date
year, month, day = get_valid_date()

# Calculate and print the digit sum of the year
sum_year = digit_sum(year)
print(f"The final sum of the digits in your birth year ({year}) is: {sum_year}")
