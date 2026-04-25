
# Boolean values
a = True
b = False
c = True

# Create a mapping of names based on the number of True values
name_mapping = {
    3: 'first',
    2: ['second', 'third', 'fourth'][int(a)*2 + int(b)],  # 2 true: second (1), third (2), fourth (3)
    1: ['fifth', 'sixth', 'seventh'][int(a)*2 + int(b)],  # 1 true: fifth (1), sixth (2), seventh (3)
    0: 'eighth'
}

# Count the number of True values
true_count = a + b + c

# Assign name based on the count of True values
name = name_mapping[true_count]

print(name)
