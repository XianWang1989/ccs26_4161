
# Boolean values
a = True
b = False
c = True

# Mapping of conditions to names
name_map = {
    (True, True, True): 'first',
    (True, True, False): 'second',
    (True, False, True): 'third',
    (True, False, False): 'fourth',
    (False, True, True): 'fifth',
    (False, True, False): 'sixth',
    (False, False, True): 'seventh',
    (False, False, False): 'eighth',
}

# Fetch the name based on the boolean values
name = name_map[(a, b, c)]

print(name)  # Output: 'third' if a=True, b=False, c=True
