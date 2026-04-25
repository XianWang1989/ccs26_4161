
def digit_sum(n):
    while n >= 10:  # Keep summing digits while n is 10 or more
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validate month and day
    if int(month) == 2 and int(day) <= 29:  # Leap year handling is not included here
        break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
        break
    elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
        break
    else:
        print("Please enter a valid input")

# Sum the digits of the year
sum_year = digit_sum(int(year))
print(f"The sum of the digits in the year is: {sum_year}")
