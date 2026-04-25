
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

sumYear = sum(map(int, str(year))) + sum(map(int, str(month))) + sum(map(int, str(day)))

while sumYear >= 10:
    sumYear = sum(map(int, str(sumYear)))

print(f"Final sum of the digits: {sumYear}")
