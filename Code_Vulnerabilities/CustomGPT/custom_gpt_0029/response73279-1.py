
sumYear = int(input("Enter a year: "))

# Continuously sum the digits until the sum is < 10
while sumYear >= 10:
    sumYear = sum(int(num) for num in str(sumYear))

print("Final sum of digits:", sumYear)
