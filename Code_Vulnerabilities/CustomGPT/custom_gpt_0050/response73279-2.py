
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Convert month and day to integers for comparison
    month_int = int(month)
    day_int = int(day)

    # Checking month and day validity
    if month_int == 2:  # February
        if day_int <= 29:  # Leap years handled elsewhere or as needed
            break
    elif month_int in (1, 3, 5, 7, 8, 10, 12) and day_int <= 31:  # 31 days
        break
    elif month_int in (4, 6, 9, 11) and day_int <= 30:  # 30 days
        break
    else:
        print("Please enter a valid input")

print("Valid date entered!")
