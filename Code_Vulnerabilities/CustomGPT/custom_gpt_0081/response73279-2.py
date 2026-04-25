
sum_year = int(year)
while sum_year >= 10:
    sum_year = sum(int(digit) for digit in str(sum_year))

print(f"The reduced sum of the digits in your birth year is: {sum_year}")
