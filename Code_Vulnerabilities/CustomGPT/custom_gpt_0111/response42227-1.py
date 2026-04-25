
def get_name(a, b, c):
    # Create a list of names based on the combination of boolean values
    names = [
        'eighth',  # (False, False, False)
        'seventh', # (False, False, True)
        'sixth',   # (False, True, False)
        'fifth',   # (False, True, True)
        'fourth',  # (True, False, False)
        'third',   # (True, False, True)
        'second',  # (True, True, False)
        'first'    # (True, True, True)
    ]

    # Calculate the index based on the boolean values
    index = (not a) * 4 + (not b) * 2 + (not c) * 1
    return names[index]

# Example usage:
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: 'third'
