
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage
year = int(input("Please enter the year you were born: "))
result = sum_digits(year)
print(f"The sum of the digits is: {result}")
