
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate date inputs
    month = int(month)
    day = int(day)

    if (month == 2 and day <= 29):
        break
    elif (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31):
        break
    elif (month in [4, 6, 9, 11] and day <= 30):
        break
    else:
        print("Please enter a valid input")

# Sum Year Logic
sumYear = sum(int(digit) for digit in year)

# Loop until sumYear is less than 10
while sumYear >= 10:
    sumYear = sum(int(digit) for digit in str(sumYear))

print("The final sum of your birth year digits is:", sumYear)
