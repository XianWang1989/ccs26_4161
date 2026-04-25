
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    month = int(month)
    day = int(day)

    # Check if the month is February
    if month == 2:
        if day <= 29:
            break
    # Check for months with 30 days
    elif month in (4, 6, 9, 11):
        if day <= 30:
            break
    # Check for months with 31 days
    elif month in (1, 3, 5, 7, 8, 10, 12):
        if day <= 31:
            break

    print("Please enter a valid date")

# Final output
print(f"You entered: {year}-{month:02d}-{day:02d}")
