
def get_valid_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        month = int(month)
        day = int(day)

        if (month == 2 and day <= 29) or \
           (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or \
           (month in [4, 6, 9, 11] and day <= 30):
            return year, month, day
        else:
            print("Please enter a valid date.")

def sum_of_digits(value):
    while value >= 10:
        value_sum = 0
        for digit in str(value):
            value_sum += int(digit)
        value = value_sum
    return value

# Get valid date input
year, month, day = get_valid_date()

# Calculate the sum of digits for year, month, and day
sum_year = sum_of_digits(int(year))
sum_month = sum_of_digits(month)
sum_day = sum_of_digits(day)

print("Final sums:")
print(f"Year: {sum_year}, Month: {sum_month}, Day: {sum_day}")
