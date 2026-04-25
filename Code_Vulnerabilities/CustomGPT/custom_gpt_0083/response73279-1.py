
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage
year = int(input("Enter your birth year: "))
result = sum_digits(year)
print("Final sum of the digits is:", result)
