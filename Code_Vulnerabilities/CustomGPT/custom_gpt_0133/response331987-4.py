
# List assignment (mutable)
list_assign = [1, 2]
list_assign[0] = 10  # Modifying the list
print(list_assign)  # Output: [10, 2]

# Tuple assignment (immutable)
tuple_assign = (1, 2)
try:
    tuple_assign[0] = 10  # This will raise an error
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment
