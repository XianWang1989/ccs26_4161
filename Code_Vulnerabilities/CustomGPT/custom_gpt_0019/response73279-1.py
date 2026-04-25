
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n
