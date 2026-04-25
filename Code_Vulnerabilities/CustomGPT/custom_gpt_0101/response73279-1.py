
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if int(month) == 2:
        if int(day) <= 29:  # Leap year handling can be added
            break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) <= 31:
            break
    elif int(month) in [4, 6, 9, 11]:
        if int(day) <= 30:
            break
    print("Please enter a valid input")

sumYear = sum(int(digit) for digit in year)

while sumYear >= 10:
    sumYear = sum(int(digit) for digit in str(sumYear))

print(sumYear)
