
# Define the mapping in a dictionary
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

# Look up the name based on (a, b, c)
name = name_mapping[(a, b, c)]

print(name)
