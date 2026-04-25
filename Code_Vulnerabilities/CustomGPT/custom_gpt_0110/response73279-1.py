
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

year = int(input("Enter your birth year: "))
result = digit_sum(year)
print(f"The reduced sum of digits is: {result}")
