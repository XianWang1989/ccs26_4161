
def get_birth_date():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        if int(month) == 2 and int(day) <= 29:
            break
        elif int(month) in {1, 3, 5, 7, 8, 10, 12} and int(day) <= 31:
            break
        elif int(month) in {4, 6, 9, 11} and int(day) <= 30:
            break
        else:
            print("Please enter a valid input")

    return year, month, day

def sum_digits(number):
    total = sum(int(digit) for digit in str(number))
    return total

def reduce_sum(value):
    while value >= 10:
        value = sum_digits(value)
    return value

# Main Code Execution
year, month, day = get_birth_date()
birth_date_sum = reduce_sum(int(year) + int(month) + int(day))
print("Final reduced sum of digits:", birth_date_sum)
