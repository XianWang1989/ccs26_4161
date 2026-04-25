
# Assume a, b, and c are your boolean values
a = True
b = False
c = True

# Create a tuple representing the boolean values
conditions = (a, b, c)

# Use a mapping to assign names based on boolean combinations
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

# Get the name using the tuple as the key
name = name_map[conditions]

print(name)  # Output will depend on the values of a, b, c
