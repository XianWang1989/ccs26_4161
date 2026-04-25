
def sum_digits(n):
    """Sums the digits of the given number until it is less than 10."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def get_valid_date():
    """Gets a valid birth date from the user."""
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        # Validate the date
        if int(month) == 2 and int(day) <= 29:
            break
        elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
            break
        elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
            break
        else:
            print("Please enter a valid input.")

    return year, month, day

# Main code
year, month, day = get_valid_date()
birth_date_sum = sum_digits(int(year) + int(month) + int(day))

print(f"The reduced sum of your birth date is: {birth_date_sum}")
