
# Function to sum digits repeatedly until less than 10
def summation(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Input and date validation loop
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    month = int(month)
    day = int(day)

    if month == 2 and day <= 29:
        break
    elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
        break
    elif month in [4, 6, 9, 11] and day <= 30:
        break
    else:
        print("Please enter a valid input")

# Calculate the sum of the inputs
birth_date_sum = summation(int(year) + month + day)
print(f"The final sum of your birth date digits is: {birth_date_sum}")
