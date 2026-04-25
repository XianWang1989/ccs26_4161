
year = int(input("Please enter the year you were born: "))

# Loop until the sum of digits is less than 10
while year >= 10:
    year = sum(int(digit) for digit in str(year))

print("Final sum of digits:", year)
