
sumYear = int(input("Enter a year (e.g., 1990): "))

while sumYear >= 10:
    sumYear = sum(int(num) for num in str(sumYear))

print(sumYear)
