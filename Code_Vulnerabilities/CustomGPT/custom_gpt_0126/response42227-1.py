
# Example boolean values
a = True
b = False
c = True

# Dictionary mapping based on the boolean values
names = {
    (True, True, True): 'first',
    (True, True, False): 'second',
    (True, False, True): 'third',
    (True, False, False): 'fourth',
    (False, True, True): 'fifth',
    (False, True, False): 'sixth',
    (False, False, True): 'seventh',
    (False, False, False): 'eighth',
}

# Retrieve the name based on the boolean values as a tuple
name = names[(a, b, c)]

print(name)
