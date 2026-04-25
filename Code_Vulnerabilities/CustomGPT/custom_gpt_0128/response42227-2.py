
# Boolean values
a = True
b = False
c = True

# Dictionary mapping of conditions
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

# Get the name based on the tuple of (a, b, c)
name = name_mapping[(a, b, c)]

print(name)  # Output: 'third'
