
# Assume you already have sumYear defined based on user input
sumYear = int(input("Enter a year: "))  # Example input

# Loop to sum the digits
while sumYear >= 10:
    sumYear = sum(int(num) for num in str(sumYear))

print(f"The final sum of the digits is: {sumYear}")
