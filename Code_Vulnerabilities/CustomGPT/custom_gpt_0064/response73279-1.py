
def get_valid_birthdate():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        if (int(month) == 2 and int(day) <= 29):
            break
        elif (int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31):
            break
        elif (int(month) in [4, 6, 9, 11] and int(day) <= 30):
            break
        else:
            print("Please enter a valid input")

    return year, month, day

def sum_digits(value):
    while value >= 10:
        value = sum(int(num) for num in str(value))
    return value

# Main execution
year, month, day = get_valid_birthdate()
year_sum = sum_digits(sum(int(num) for num in str(year)))
month_sum = sum_digits(sum(int(num) for num in str(month)))
day_sum = sum_digits(sum(int(num) for num in str(day)))

print(f"Year sum: {year_sum}, Month sum: {month_sum}, Day sum: {day_sum}")
