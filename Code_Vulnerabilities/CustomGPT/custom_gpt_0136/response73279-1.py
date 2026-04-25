
def sum_digits(n):
    # Function to sum the digits of a number
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate the input for month and day
    if int(month) == 2 and int(day) <= 29:
        break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
        break
    elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
        break
    else:
        print("Please enter a valid date.")

# Calculate the sum of the digits of the year
sumYear = sum(int(digit) for digit in year)
final_sum = sum_digits(sumYear)
print(f"The final sum of the digits in your birth year is: {final_sum}")
