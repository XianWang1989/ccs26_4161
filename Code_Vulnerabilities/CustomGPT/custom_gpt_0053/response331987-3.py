
a, b = (1, 2)
# a tuple cannot be modified
try:
    a[0] = 3  # This will raise TypeError
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment
