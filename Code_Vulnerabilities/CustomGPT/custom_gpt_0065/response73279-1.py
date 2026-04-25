
def sum_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

# Example usage
sumYear = int(input("Enter the year you were born: "))
result = sum_digits(sumYear)
print(result)
