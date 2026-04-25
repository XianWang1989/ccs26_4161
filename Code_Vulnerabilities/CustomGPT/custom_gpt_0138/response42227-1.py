
def get_name(a, b, c):
    return (
        'eighth',  # 000
        'seventh', # 001
        'sixth',   # 010
        'fifth',   # 011
        'fourth',  # 100
        'third',   # 101
        'second',  # 110
        'first'    # 111
    )[(a << 2) + (b << 1) + c]

# Example usage:
a = True
b = False
c = True
name = get_name(a, b, c)
print(name)  # Output will be 'third'
