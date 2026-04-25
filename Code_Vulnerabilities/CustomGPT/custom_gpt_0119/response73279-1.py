
def get_birth_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        if int(month) == 2 and int(day) <= 29:
            break
        elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
            break
        elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
            break
        else:
            print("Please enter a valid input.")

    return year, month, day

def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Get date from user
year, month, day = get_birth_date()

# Calculate the sum of the digits in the year
sum_year = sum(int(digit) for digit in year)
final_sum = digit_sum(sum_year)

print(f"The final sum of the digits in your year of birth ({year}) is: {final_sum}")
