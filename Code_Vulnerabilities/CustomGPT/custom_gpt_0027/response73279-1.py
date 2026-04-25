
sumYear = int(input("Enter a year: "))
while sumYear >= 10:
    sumYear = sum(int(num) for num in str(sumYear))

print(sumYear)
