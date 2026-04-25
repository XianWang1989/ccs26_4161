
year = int(input("Please enter the year you were born: "))
while year >= 10:
    year = sum(int(digit) for digit in str(year))
print("Sum of digits:", year)
