
def get_name(a, b, c):
    # Create a tuple with names that correspond to all possible True/False combinations
    name_options = (
        'eighth',  # 0b000 -> all False
        'seventh', # 0b001 -> c is True
        'sixth',   # 0b010 -> b is True
        'fifth',   # 0b011 -> b and c are True
        'fourth',  # 0b100 -> a is True
        'third',   # 0b101 -> a and c are True
        'second',  # 0b110 -> a and b are True
        'first'    # 0b111 -> a, b, and c are True
    )

    # Calculate the index by treating a, b, and c as binary digits
    index = (a << 2) | (b << 1) | c 

    # Use the index to get the corresponding name
    return name_options[index]

# Example usage:
a = True
b = False
c = True
name = get_name(a, b, c)
print(name)  # Output will be 'third'
