
# Define the booleans
a = True
b = False
c = True

# Map the boolean combinations to their respective names
names = {
    (True, True, True): 'first',
    (True, True, False): 'second',
    (True, False, True): 'third',
    (True, False, False): 'fourth',
    (False, True, True): 'fifth',
    (False, True, False): 'sixth',
    (False, False, True): 'seventh',
    (False, False, False): 'eighth'
}

# Use the tuple of (a, b, c) to get the corresponding name
name = names[(a, b, c)]

print(name)  # This will print the corresponding name based on the boolean values
