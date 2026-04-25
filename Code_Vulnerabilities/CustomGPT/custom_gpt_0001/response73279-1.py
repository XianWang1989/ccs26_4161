
# Function to calculate the sum of the digits of a number
def digit_sum(num):
    sum_digits = sum(int(digit) for digit in str(num))
    return sum_digits

# Loop until a valid date is provided
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if int(month) == 2 and int(day) <= 29:
        break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
        break
    elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
        break
    else:
        print("Please enter a valid input.")

# Calculate the sum of the digits of the year
sumYear = sum(int(digit) for digit in year)

# Continuously sum the digits until it is less than 10
while sumYear >= 10:
    sumYear = digit_sum(sumYear)

print(f"The final sum of the digits of your birth year is: {sumYear}")
