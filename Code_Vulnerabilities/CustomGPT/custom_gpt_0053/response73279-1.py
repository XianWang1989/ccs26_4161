
# Function to sum the digits of a number and reduce it until it's less than 10
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Main program to get user input and validate date
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if int(month) == 2:
        if int(day) <= 29:  # February considers leap years implicitly by allowing 29
            break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) <= 31:
            break
    elif int(month) in [4, 6, 9, 11]:
        if int(day) <= 30:
            break
    else:
        print("Please enter a valid input")

# Calculate the sum of the digits of the year
sumYear = sum_digits(int(year))
print(f"The reduced sum of the digits in the year is: {sumYear}")
