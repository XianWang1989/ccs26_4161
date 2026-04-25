
sumYear = int(input("Please enter the year you were born: "))

# Repeat the summation process until sumYear is less than 10
while sumYear >= 10:
    sumYear = sum(int(num) for num in str(sumYear))

print(f"The reduced sum of the digits of your birth year is: {sumYear}")
