
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage
year = int(input("Please enter the year you were born: "))
sumYear = sum_digits(year)
print("Final sum of year digits:", sumYear)
