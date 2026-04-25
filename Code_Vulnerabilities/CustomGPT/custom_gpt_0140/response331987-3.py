
try:
    [a, b] = [1, 2, 3]  # This will raise an error
except ValueError as e:
    print(e)  # Output: not enough values to unpack (expected 2, got 3)

try:
    a, b = [1, 2, 3]  # This works without issue but only assigns the first two
    print(a, b)  # Output: 1 2
except ValueError as e:
    print(e)
