
def get_valid_birthday():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        # Validate the date inputs
        if int(month) == 2 and int(day) <= 29:
            break
        elif int(month) in {1, 3, 5, 7, 8, 10, 12} and int(day) <= 31:
            break
        elif int(month) in {4, 6, 9, 11} and int(day) <= 30:
            break
        else:
            print("Please enter a valid input")

    return year, month, day

def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

year, month, day = get_valid_birthday()

# Calculate and print the sum of digits for the year, month, and day
for value in (year, month, day):
    total_sum = digit_sum(sum(int(digit) for digit in value))
    print(f"Sum of digits for {value}: {total_sum}")
