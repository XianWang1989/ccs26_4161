
def sum_of_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))  # Re-sum digits if >= 10
    return n

year = 0
while year < 1000:  # Ensuring a plausible year
    month = input("Please enter the month you were born (1-12): ")
    day = input("Please enter the day you were born: ")

    if int(month) == 2 and int(day) <= 29:
        break
    elif int(month) in {1, 3, 5, 7, 8, 10, 12} and int(day) <= 31:
        break
    elif int(month) in {4, 6, 9, 11} and int(day) <= 30:
        break
    else:
        print("Please enter a valid input")

# Now let's sum the digits of the year
year = int(input("Please enter the year you were born: "))
result = sum_of_digits(year)
print("Sum of digits:", result)
