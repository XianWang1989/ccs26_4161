
def get_birth_date():
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
            print("Please enter a valid input")

    return year

def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Get the birth year
birth_year = get_birth_date()
# Convert year to integer and calculate the sum of its digits
sum_year = digit_sum(int(birth_year))
print(f"The reduced digit sum of your birth year is: {sum_year}")
