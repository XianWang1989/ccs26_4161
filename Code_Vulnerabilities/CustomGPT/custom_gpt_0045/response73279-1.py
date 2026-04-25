
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate date
    month = int(month)
    day = int(day)
    if month == 2 and day <= 29:
        break
    elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
        break
    elif month in [4, 6, 9, 11] and day <= 30:
        break
    else:
        print("Please enter a valid input")

# Example of using the digit sum function on the inputs
birth_date_sum = digit_sum(int(year)) + digit_sum(month) + digit_sum(day)
print(f"The final digit sum of your birth date is: {birth_date_sum}")
