
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage:
sumYear = int(input("Enter a year: "))
result = digit_sum(sumYear)
print(result)
