
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

year = 2022  # This could be your input year
result = sum_digits(year)
print(result)
