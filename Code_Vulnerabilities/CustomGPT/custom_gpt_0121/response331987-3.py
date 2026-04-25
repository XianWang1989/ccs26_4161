
# List assignment
result_list = [x * 2 for x in range(3)]
[a, b, c] = result_list
print(a, b, c)  # Output: 0 2 4

# Tuple assignment
result_tuple = (x * 2 for x in range(3))  # Using a generator
a, b, c = result_tuple  # Works with unpacking as well
print(a, b, c)  # Output might vary if generator is exhausted
