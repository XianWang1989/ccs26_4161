
def sum_digits(num):
    while num >= 10:  # Continue until the number is a single digit
        num = sum(int(digit) for digit in str(num))
    return num

# Example usage
sumYear = int(input("Enter a year: "))
result = sum_digits(sumYear)
print(result)
