
year = int(input("Please enter the birth year: "))
sumYear = year

while sumYear >= 10:
    sumYear = sum(int(num) for num in str(sumYear))

print("The reduced sum is:", sumYear)
