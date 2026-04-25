
# Assume you already have sumYear defined based on user input
sumYear = int(input("Enter a year: "))  # Example input

# Loop to sum the digits
while sumYear >= 10:
    total = 0
    for num in str(sumYear):
        total += int(num)
    sumYear = total

print(f"The final sum of the digits is: {sumYear}")
