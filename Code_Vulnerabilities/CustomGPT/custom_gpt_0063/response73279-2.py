
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    month_int = int(month)
    day_int = int(day)

    if month_int == 2 and day_int <= 29:
        break
    elif month_int in [1, 3, 5, 7, 8, 10, 12] and day_int <= 31:
        break
    elif month_int in [4, 6, 9, 11] and day_int <= 30:
        break
    else:
        print("Please enter a valid input")
