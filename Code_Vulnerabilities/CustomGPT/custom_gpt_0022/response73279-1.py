
# Function to calculate the sum of digits until it's less than 10
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Loop to validate the birthdate input
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate input for month and day
    if int(month) == 2 and int(day) <= 29:
        break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
        break
    elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
        break
    else:
        print("Please enter a valid input")

# Example usage of the digit summation
sum_year = sum_digits(int(year))
print("Summed year digits:", sum_year)
