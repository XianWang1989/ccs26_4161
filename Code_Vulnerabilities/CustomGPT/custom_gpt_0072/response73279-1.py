
def get_valid_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        # Validate day based on the month
        if int(month) == 2 and int(day) <= 29:  # Check for February (leap year not considered for simplicity)
            break
        elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
            break
        elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
            break
        else:
            print("Please enter a valid input")

    return int(year)

def sum_digits(n):
    total = n
    while total >= 10:
        total = sum(int(digit) for digit in str(total))
    return total

# Get the user input and calculate the summed digits
year = get_valid_date()
result = sum_digits(year)
print(f"The reduced sum of the year is: {result}")
