
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage
year = int(input("Enter your birth year: "))
summed_year = sum_digits(year)
print(f"Sum of the digits in your birth year: {summed_year}")
