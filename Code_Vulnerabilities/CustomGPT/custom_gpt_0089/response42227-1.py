
# Define the boolean values
a = True
b = False
c = True

# Create a dictionary that maps (a, b, c) tuples to names
name_mapping = {
    (True, True, True): 'first',
    (True, True, False): 'second',
    (True, False, True): 'third',
    (True, False, False): 'fourth',
    (False, True, True): 'fifth',
    (False, True, False): 'sixth',
    (False, False, True): 'seventh',
    (False, False, False): 'eighth'
}

# Assign the name based on the boolean tuple
name = name_mapping[(a, b, c)]

print(name)  # Output: 'third'
