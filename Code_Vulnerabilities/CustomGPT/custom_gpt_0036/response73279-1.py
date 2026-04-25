
def digit_sum(n):
    while n >= 10:  # Continue summing until n is less than 10
        n = sum(int(digit) for digit in str(n))  # Sum the digits
    return n

# Example usage
birth_year = 1995  # Assume this is inputted earlier
sum_of_digits = digit_sum(birth_year)
print("Final sum of digits:", sum_of_digits)
