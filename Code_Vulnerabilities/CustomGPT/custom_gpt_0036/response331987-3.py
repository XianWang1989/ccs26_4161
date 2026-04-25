
# List Assignment
[a, b] = [1, 2]
print("List Assignment: ")
print("a:", a)  # Output: a: 1
print("b:", b)  # Output: b: 2

# Tuple Assignment
a, b = [3, 4]
print("\nTuple Assignment: ")
print("a:", a)  # Output: a: 3
print("b:", b)  # Output: b: 4

# Mutability Demonstration
my_list = [5, 6]
my_list[0] = 10  # This is valid because lists are mutable
print("\nModified List: ", my_list)  # Output: Modified List:  [10, 6]

# Attempt to modify tuple (by creating a new one)
my_tuple = (5, 6)
try:
    my_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print("\nError: ", e)  # Output: Error:  'tuple' object does not support item assignment
