
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage
year = int(input("Please enter the year you were born: "))
result = digit_sum(year)
print(f"Final sum of digits: {result}")
