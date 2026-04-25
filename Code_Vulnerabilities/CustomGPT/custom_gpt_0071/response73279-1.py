
def sum_of_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

year = int(input("Please enter the year you were born: "))
result = sum_of_digits(year)
print("Final sum of birth year digits:", result)
