
def get_birth_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        # Validate the date
        if int(month) == 2 and int(day) <= 29:
            break
        elif int(month) in {1, 3, 5, 7, 8, 10, 12} and int(day) <= 31:
            break
        elif int(month) in {4, 6, 9, 11} and int(day) <= 30:
            break
        else:
            print("Please enter a valid input")

    return year, month, day

def sum_digits(value):
    while value >= 10:
        value = sum(int(digit) for digit in str(value))
    return value

year, month, day = get_birth_date()
total = sum_digits(int(year) + int(month) + int(day))
print(f"The final sum of the digits is: {total}")
