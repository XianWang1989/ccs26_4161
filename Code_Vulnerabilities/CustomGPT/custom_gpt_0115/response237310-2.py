
# Initialize a consistent object
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

# Change the state to inconsistent
x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'
