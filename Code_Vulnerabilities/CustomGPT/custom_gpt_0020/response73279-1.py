
def get_birth_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        # Validate date
        if int(month) == 2 and int(day) <= 29:
            break
        elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
            break
        elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
            break
        else:
            print("Please enter a valid input")

    return int(year)

def sum_digits(num):
    while num >= 10:  # Continue until the sum is less than 10
        num = sum(int(digit) for digit in str(num))  # Use generator expression for clean code
    return num

# Getting the year and calculating the digit sum
birth_year = get_birth_date()
final_sum = sum_digits(birth_year)

print(f"The final sum of the digits in the year {birth_year} is: {final_sum}")
