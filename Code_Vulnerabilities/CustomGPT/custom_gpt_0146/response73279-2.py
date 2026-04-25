
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if int(month) == 2:
        if int(day) <= 29:  # Adjusted for leap year consideration as needed
            break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:  # Days in months with 31 days
        if int(day) <= 31:
            break
    elif int(month) in [4, 6, 9, 11]:  # Days in months with 30 days
        if int(day) <= 30:
            break
    else:
        print("Please enter a valid input")

print(f"You entered the date: {year}-{month}-{day}")
