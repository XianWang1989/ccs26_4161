
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    month = int(month)
    day = int(day)

    if month == 2:
        if day <= 29:  # Consider leap years as necessary
            break
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day <= 31:
            break
    elif month in [4, 6, 9, 11]:
        if day <= 30:
            break
    else:
        print("Please enter a valid input")
