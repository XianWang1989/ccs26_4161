
# Function to validate the birth date
def get_birth_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born (1-12): ")
        day = input("Please enter the day you were born (1-31): ")

        if (int(month) == 2 and int(day) <= 29) or \
           (int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31) or \
           (int(month) in [4, 6, 9, 11] and int(day) <= 30):
            return year
        else:
            print("Please enter a valid input.")

# Function to sum digits of the year
def sum_year_digits(year):
    sumYear = sum(int(digit) for digit in year)
    while sumYear >= 10:
        sumYear = sum(int(digit) for digit in str(sumYear))
    return sumYear

# Main part of the program
year = get_birth_date()
result = sum_year_digits(year)
print(f"The final sum of the digits is: {result}")
