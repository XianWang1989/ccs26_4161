
def assign_name(a, b, c):
    # Create a list where each index corresponds to the boolean values
    # Index: 0 for (False, False, False) to 7 for (True, True, True)
    names = [
        'eighth',  # 000
        'seventh', # 001
        'sixth',   # 010
        'fifth',   # 011
        'fourth',  # 100
        'third',   # 101
        'second',  # 110
        'first'    # 111
    ]

    # Calculate the index based on the boolean values
    index = (a << 2) | (b << 1) | c
    return names[index]

# Example usage
a, b, c = True, False, True
name = assign_name(a, b, c)
print(name)  # Output: 'third'
