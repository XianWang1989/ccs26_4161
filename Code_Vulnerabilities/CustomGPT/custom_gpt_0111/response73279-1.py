
def get_valid_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        if int(month) == 2 and int(day) <= 29:
            break
        elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
            break
        elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
            break
        else:
            print("Please enter a valid date.")

    return year, month, day

def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Get valid birth date
year, month, day = get_valid_date()

# Sum the digits of the year
sum_year = sum_digits(int(year))
print(f"The sum of the digits of your year of birth is: {sum_year}")
