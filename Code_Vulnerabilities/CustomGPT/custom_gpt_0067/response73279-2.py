
while True:
    year = input("Please enter the year you were born: ")
    month = int(input("Please enter the month you were born (1-12): "))
    day = int(input("Please enter the day you were born (1-31): "))

    if (month == 2 and day <= 29) or \
       (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or \
       (month in [4, 6, 9, 11] and day <= 30):
        break
    else:
        print("Please enter a valid date")
