
# Sample boolean values
a = True
b = False
c = True

# Mapping of boolean combinations to names
mapping = {
    (True, True, True): 'first',
    (True, True, False): 'second',
    (True, False, True): 'third',
    (True, False, False): 'fourth',
    (False, True, True): 'fifth',
    (False, True, False): 'sixth',
    (False, False, True): 'seventh',
    (False, False, False): 'eighth'
}

# Get the name based on the boolean values
name = mapping[(a, b, c)]

print(name)  # Output: 'third'
