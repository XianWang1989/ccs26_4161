
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    # Validating the date
    if int(month) == 2:
        if int(day) <= 29:  # Leap year check can be added if needed
            break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) <= 31:
            break
    elif int(month) in [4, 6, 9, 11]:
        if int(day) <= 30:
            break
    else:
        print("Please enter a valid input")

# Calculate the sum of digits for the year
sum_year = digit_sum(int(year))
print(f"The digit sum of your birth year is: {sum_year}")
