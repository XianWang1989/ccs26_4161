
def sum_of_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage
year = int(input("Please enter the year you were born: "))
summed_year = sum_of_digits(year)
print(f"The summed year is: {summed_year}")
