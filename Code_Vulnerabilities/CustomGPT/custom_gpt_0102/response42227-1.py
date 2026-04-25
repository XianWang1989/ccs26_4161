
# Assume a, b, and c are your boolean values
a, b, c = True, False, True  # example values

# Define a mapping of indices to names
name_mapping = {
    (True, True, True): 'first',
    (True, True, False): 'second',
    (True, False, True): 'third',
    (True, False, False): 'fourth',
    (False, True, True): 'fifth',
    (False, True, False): 'sixth',
    (False, False, True): 'seventh',
    (False, False, False): 'eighth',
}

# Use the tuple of booleans to find the name
name = name_mapping[(a, b, c)]

print(name)  # Output: 'third'
