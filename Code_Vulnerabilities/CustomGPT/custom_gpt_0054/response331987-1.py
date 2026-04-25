
# List assignment
[a, b] = [1, 2]
print("List Assignment:")
print("a:", a)  # Output: a: 1
print("b:", b)  # Output: b: 2

# Tuple assignment
x, y = 3, 4
print("\nTuple Assignment:")
print("x:", x)  # Output: x: 3
print("y:", y)  # Output: y: 4

# Demonstrating mutability and immutability
my_list = [1, 2, 3]
my_list[0] = 10  # This is allowed
print("\nModified List:", my_list)  # Output: Modified List: [10, 2, 3]

my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise a TypeError because tuples cannot be modified
