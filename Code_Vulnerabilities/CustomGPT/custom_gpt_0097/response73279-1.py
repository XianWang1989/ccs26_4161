
def sum_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

while True:
    year = input("Please enter the year you were born: ")
    month = input("Please enter the month you were born: ")
    day = input("Please enter the day you were born: ")

    if month == '02' and int(day) <= 29:
        break
    elif month in ['01', '03', '05', '07', '08', '10', '12'] and int(day) <= 31:
        break
    elif month in ['04', '06', '09', '11'] and int(day) <= 30:
        break
    else:
        print("Please enter a valid input")

# Example usage
birth_year = int(year)
digit_sum = sum_digits(birth_year)
print(f"The final digit sum of the year is: {digit_sum}")
