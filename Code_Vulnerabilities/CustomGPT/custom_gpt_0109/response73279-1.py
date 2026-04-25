
def get_valid_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        # Validate months and days
        month, day = int(month), int(day)
        if month == 2 and day <= 29:
            break
        elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
            break
        elif month in [4, 6, 9, 11] and day <= 30:
            break
        else:
            print("Please enter a valid input")

    return year

def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

year = get_valid_date()
year_sum = digit_sum(int(year))

print(f"Final reduced sum of year digits: {year_sum}")
