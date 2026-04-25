
year = input("Please enter the year you were born: ")
sumYear = sum(int(digit) for digit in year)

while sumYear >= 10:
    sumYear = sum(int(digit) for digit in str(sumYear))

print("Final sum of digits:", sumYear)
