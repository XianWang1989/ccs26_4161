
# Function to sum the digits of a number until the sum is less than 10
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))  # Convert to string, sum the digits
    return n

# Example usage
birth_year = input("Please enter the birth year: ")
sum_year = sum_digits(int(birth_year))
print(f"The final digit sum is: {sum_year}")
