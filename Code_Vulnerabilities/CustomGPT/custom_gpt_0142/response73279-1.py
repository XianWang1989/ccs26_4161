
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

year = int(input("Please enter your birth year: "))
result = sum_digits(year)
print("Sum of the digits:", result)
