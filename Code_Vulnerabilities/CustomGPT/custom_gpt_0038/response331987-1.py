
# List assignment
list_values = [1, 2]
a, b = list_values
print(f'a: {a}, b: {b}')  # Output: a: 1, b: 2

# Tuple assignment (using a list)
tuple_values = [3, 4]
x, y = tuple_values
print(f'x: {x}, y: {y}')  # Output: x: 3, y: 4

# Tuple assignment (using a tuple)
tuple_values2 = (5, 6)
m, n = tuple_values2
print(f'm: {m}, n: {n}')  # Output: m: 5, n: 6

# Comparing mutability
list_example = [7, 8]
list_example[0] = 10  # Mutable
print(list_example)  # Output: [10, 8]

# Tuple example
tuple_example = (9, 10)
# tuple_example[0] = 12  # This will raise a TypeError since tuples are immutable
