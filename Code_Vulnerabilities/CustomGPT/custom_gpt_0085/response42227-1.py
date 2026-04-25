
# Example booleans
a = True
b = False
c = True

# Create a dictionary to map boolean combinations to names
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

# Use a tuple to represent the values of a, b, c
name = name_map[(a, b, c)]

print(name)  # Output will be 'third' if a=True, b=False, c=True
