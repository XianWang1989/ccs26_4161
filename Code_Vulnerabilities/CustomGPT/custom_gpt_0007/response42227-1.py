
# Boolean values
a = True  # Example value
b = False  # Example value
c = True  # Example value

# Create a mapping of boolean combinations to names
name_map = {
    (True, True, True): 'first',
    (True, True, False): 'second',
    (True, False, True): 'third',
    (True, False, False): 'fourth',
    (False, True, True): 'fifth',
    (False, True, False): 'sixth',
    (False, False, True): 'seventh',
    (False, False, False): 'eighth'
}

# Use tuple to get the corresponding name
name = name_map[(a, b, c)]

print(name)  # Outputs the corresponding name based on the booleans
