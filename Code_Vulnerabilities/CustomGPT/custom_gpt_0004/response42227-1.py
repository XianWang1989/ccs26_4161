
# Booleans
a = True
b = False
c = True

# Mapping names based on the number of True values
names = (
    'eighth',   # 0 True
    'seventh',  # 1 True
    'sixth',    # 2 True
    'fifth',    # 3 True
    'fourth',   # 4 True
    'third',    # 5 True
    'second',   # 6 True
    'first'     # 7 True
)

# Count the True values
true_count = sum((a, b, c))

# Assign name based on the count of True values
name = names[true_count]

print(name)  # Output will depend on the values of a, b, and c
