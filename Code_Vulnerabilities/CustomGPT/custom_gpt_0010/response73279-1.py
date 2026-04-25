
def get_valid_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        if int(month) == 2:
            if int(day) <= 29:
                break
        elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
            if int(day) <= 31:
                break
        elif int(month) in [4, 6, 9, 11]:
            if int(day) <= 30:
                break
        print("Please enter a valid input")

    return int(year), int(month), int(day)

def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

year, month, day = get_valid_date()
birth_date_sum = sum_digits(year + month + day)
print("Sum of digits:", birth_date_sum)
