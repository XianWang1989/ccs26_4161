
def sum_of_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def main():
    while True:
        year = input("Please enter the year you were born: ")
        month = input("Please enter the month you were born: ")
        day = input("Please enter the day you were born: ")

        # Check for leap year conditions for February
        if (int(month) == 2):
            if (int(day) <= 29 and (int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0))):
                break
            elif (int(day) <= 28):
                break
        # Check for days in months with 31 days
        elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
            if int(day) <= 31:
                break
        # Check for days in months with 30 days
        elif int(month) in [4, 6, 9, 11]:
            if int(day) <= 30:
                break
        else:
            print("Please enter a valid input")

    # Sum the digits of the year
    sumYear = sum_of_digits(int(year))
    print(f"The sum of the digits of your birth year is: {sumYear}")

main()
