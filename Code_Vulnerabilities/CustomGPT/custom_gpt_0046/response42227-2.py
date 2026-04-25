
def get_name(a, b, c):
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
    return name_map[(a, b, c)]

# Example usage:
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: 'third'
