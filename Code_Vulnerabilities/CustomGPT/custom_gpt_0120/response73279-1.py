
def sum_digits(value):
    total = 0
    for num in str(value):
        total += int(num)
    return total

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if (int(month) == 2 and int(day) <= 29) or \
       (int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31) or \
       (int(month) in [4, 6, 9, 11] and int(day) <= 30):
        break
    else:
        print("Please enter a valid input")

# Sum individual digits of the year
sumYear = sum_digits(year)

# Loop to sum digits until it's less than 10
while sumYear >= 10:
    sumYear = sum_digits(sumYear)

print("Final digit sum of the year:", sumYear)
