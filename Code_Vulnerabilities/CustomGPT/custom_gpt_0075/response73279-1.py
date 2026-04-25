
def get_birth_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        if (month == '2' and int(day) <= 29) or \
           (month in ['1', '3', '5', '7', '8', '10', '12'] and int(day) <= 31) or \
           (month in ['4', '6', '9', '11'] and int(day) <= 30):
            break
        else:
            print("Please enter a valid input")

    return year, month, day

def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Main execution
year, month, day = get_birth_date()
date_sum = sum_digits(int(year) + int(month) + int(day))
print(f"The final sum of digits is: {date_sum}")
