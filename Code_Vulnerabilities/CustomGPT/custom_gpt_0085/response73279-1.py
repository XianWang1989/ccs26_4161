
# Function to sum digits until the sum is less than 10
def sum_digits_until_less_than_ten(value):
    while value >= 10:
        value = sum(int(digit) for digit in str(value))
    return value

# Birth date input and validation
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    month = int(month)
    day = int(day)

    if month == 2 and day <= 29:  # Leap year not considered here
        break
    elif month in {1, 3, 5, 7, 8, 10, 12} and day <= 31:
        break
    elif month in {4, 6, 9, 11} and day <= 30:
        break
    else:
        print("Please enter a valid input")

# Calculate and print the reduced year sum
sumYear = int(year)
final_sum = sum_digits_until_less_than_ten(sumYear)
print("Final reduced sum of the birth year digits:", final_sum)
