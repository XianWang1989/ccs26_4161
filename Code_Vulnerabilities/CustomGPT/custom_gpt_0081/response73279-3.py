
while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if int(month) == 2:
        if int(day) <= 29:  # You may want to check for leap years as needed
            break
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) <= 31:
            break
    elif int(month) in [4, 6, 9, 11]:
        if int(day) <= 30:
            break
    else:
        print("Please enter a valid input")

# Summing the digits of the year
sum_year = int(year)
while sum_year >= 10:
    sum_year = sum(int(digit) for digit in str(sum_year))

print(f"The reduced sum of the digits in your birth year is: {sum_year}")
