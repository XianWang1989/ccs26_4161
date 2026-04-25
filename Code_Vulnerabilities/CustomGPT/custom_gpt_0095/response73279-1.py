
def sum_digits(number):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number

# Example usage
year = int(input("Please enter the year you were born: "))
result = sum_digits(year)
print(f'Sum of digits: {result}')
