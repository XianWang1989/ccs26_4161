
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born (1-12): ")
    day = input("Please enter the day you were born (1-31): ")

    month = int(month)
    day = int(day)

    if month == 2 and day <= 29:  # Does not check for leap years; consider adding that check
        break
    elif month in {1, 3, 5, 7, 8, 10, 12} and day <= 31:
        break
    elif month in {4, 6, 9, 11} and day <= 30:
        break
    else:
        print("Please enter a valid input")

print(f"You entered a valid date: {day}/{month}/{year}")
