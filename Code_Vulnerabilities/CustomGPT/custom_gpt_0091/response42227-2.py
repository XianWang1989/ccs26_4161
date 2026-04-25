
# Assuming a, b, c are your boolean variables
a, b, c = True, False, True  # Example values

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

name = name_map[(a, b, c)]
print(name)
