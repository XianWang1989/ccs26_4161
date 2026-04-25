
# Assuming a, b, c are your boolean variables
a, b, c = True, False, True  # Example values

name = [
    'eighth',  # 0: not a, not b, not c
    'seventh', # 1: not a, not b, c
    'sixth',   # 2: not a, b, not c
    'fifth',   # 3: not a, b, c
    'fourth',  # 4: a, not b, not c
    'third',   # 5: a, not b, c
    'second',  # 6: a, b, not c
    'first'    # 7: a, b, c
][4 * a + 2 * b + c]

print(name)  # This will print 'third' based on the example values
