
def get_birthday():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        # Validate the date
        if int(month) == 2:
            if int(day) <= 29:
                break
        elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
            if int(day) <= 31:
                break
        elif int(month) in [4, 6, 9, 11]:
            if int(day) <= 30:
                break
        else:
            print("Please enter a valid input")

    return year, month, day

def sum_digits(value):
    total = sum(int(digit) for digit in str(value))
    while total >= 10:
        total = sum(int(digit) for digit in str(total))
    return total

# Main execution
year, month, day = get_birthday()
birth_sum = sum_digits(year) + sum_digits(month) + sum_digits(day)

print(f"The final sum of your birth date digits is: {birth_sum}")
