
print(foo([-4]))
# Output: [ (4, -4) ]

print(foo([1, 1]))
# Output: [ (1, 1), (1, -1), (-1, 1), (-1, -1) ]

print(foo([-1, 3]))
# Output: [ (-1, 3), (-1, -3), (1, 3), (1, -3) ]

print(foo([1, -1, 1]))
# Output: All combinations for [1, -1, 1]
