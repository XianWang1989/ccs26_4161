
def get_birth_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        # Validate date input
        if int(month) == 2 and int(day) <= 29:
            break
        elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:
            break
        elif int(month) in [4, 6, 9, 11] and int(day) <= 30:
            break
        else:
            print("Please enter a valid input")

    # Summing the digits in birth date
    total_sum = int(year) + int(month) + int(day)

    # Sum digits until less than 10
    while total_sum >= 10:
        total_sum = sum(int(digit) for digit in str(total_sum))

    print("Final sum of digits:", total_sum)

get_birth_date()
