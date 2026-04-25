
while True:
    year = input("Please enter the year you were born: ")
    month = int(input("Please enter the month you were born: "))
    day = int(input("Please enter the day you were born: "))

    if month == 2 and day <= 29:
        break
    elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
        break
    elif month in [4, 6, 9, 11] and day <= 30:
        break
    else:
        print("Please enter a valid input")

print(f"Your birth date is: {day}/{month}/{year}")
