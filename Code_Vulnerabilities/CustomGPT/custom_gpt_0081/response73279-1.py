
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Input validation for days in months
    if int(month) == 2:
        if int(day) <= 29:  # You may want further checks for leap years if needed
            break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:  # Months with 31 days
        if int(day) <= 31:
            break
    elif int(month) in [4, 6, 9, 11]:  # Months with 30 days
        if int(day) <= 30:
            break
    else:
        print("Please enter a valid input")
