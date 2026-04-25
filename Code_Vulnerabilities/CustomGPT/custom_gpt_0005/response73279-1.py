
# Function to sum digits until the result is less than 10
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Input loop for birth date
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if int(month) == 2 and int(day) <= 29:  # Leap year logic can be added if needed
        break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
        break
    elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
        break
    else:
        print("Please enter a valid input")

# Calculate the digit sum of the year
result = sum_digits(int(year))
print(f"The final sum of the digits in your birth year is: {result}")
