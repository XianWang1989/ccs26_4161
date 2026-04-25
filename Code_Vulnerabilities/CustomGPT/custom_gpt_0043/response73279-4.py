
# Date Input
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if int(month) == 2:
        if int(day) <= 29:
            break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) <= 31:
            break
    elif int(month) in [4, 6, 9, 11]:
        if int(day) <= 30:
            break
    else:
        print("Please enter a valid input")

# Summation
sumYear = int(year)  # Using the year as your input to sum
while sumYear >= 10:
    total = 0
    for num in str(sumYear):
        total += int(num)
    sumYear = total

print(f"The final sum of the digits is: {sumYear}")
