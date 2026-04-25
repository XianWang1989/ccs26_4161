
def get_name(a, b, c):
    # Create a mapping from boolean tuples to names
    mapping = {
        (True, True, True): 'first',
        (True, True, False): 'second',
        (True, False, True): 'third',
        (True, False, False): 'fourth',
        (False, True, True): 'fifth',
        (False, True, False): 'sixth',
        (False, False, True): 'seventh',
        (False, False, False): 'eighth',
    }

    # Get the name based on the boolean values
    return mapping[(a, b, c)]

# Example usage
a = True
b = False
c = True
name = get_name(a, b, c)
print(name)  # Output: 'third'
