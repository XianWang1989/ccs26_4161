
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))  # Repeating until n is a single digit
    return n

year = int(input("Please enter the year you were born: "))
result = digit_sum(year)
print(result)
