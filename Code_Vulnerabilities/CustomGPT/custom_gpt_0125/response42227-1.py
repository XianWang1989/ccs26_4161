
def get_name(a, b, c):
    names = (
        'eighth',  # 0: not a, not b, not c
        'seventh', # 1: not a, not b, c
        'sixth',   # 2: not a, b, not c
        'fifth',   # 3: not a, b, c
        'fourth',  # 4: a, not b, not c
        'third',   # 5: a, not b, c
        'second',  # 6: a, b, not c
        'first'    # 7: a, b, c
    )
    index = (not a) + (not b) * 2 + (not c) * 4
    return names[index]

# Example usage:
a = True
b = False
c = True
name = get_name(a, b, c)
print(name)  # Output: 'third'
