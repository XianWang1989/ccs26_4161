
# Creating a consistent object
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

# Modifying to create inconsistency
x.a = 2
print(str(x))  # Output: 'Sum(2, 2) + ' # sum=3''
