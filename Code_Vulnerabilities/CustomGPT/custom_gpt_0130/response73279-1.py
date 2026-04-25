
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

year = int(input("Please enter the year you were born: "))
# Use the digit_sum function on the year
final_sum_year = digit_sum(year)
print(final_sum_year)
