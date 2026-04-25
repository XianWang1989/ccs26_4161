
def get_name(a, b, c):
    # Define the mapping as a list of tuples
    conditions = [
        (True, True, True, 'first'),
        (True, True, False, 'second'),
        (True, False, True, 'third'),
        (True, False, False, 'fourth'),
        (False, True, True, 'fifth'),
        (False, True, False, 'sixth'),
        (False, False, True, 'seventh'),
        (False, False, False, 'eighth'),
    ]

    # Iterate through the conditions and return the matching name
    for cond in conditions:
        if (a, b, c) == cond[:3]:
            return cond[3]

    return None  # Fallback in case no conditions match

# Example usage
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: 'third'
