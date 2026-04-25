
# Assume a, b, and c are your boolean variables
result = ( 
    'eighth',  # (False, False, False)
    'seventh', # (False, False, True)
    'sixth',   # (False, True, False)
    'fifth',   # (False, True, True)
    'fourth',  # (True, False, False)
    'third',   # (True, False, True)
    'second',  # (True, True, False)
    'first'    # (True, True, True)
)

# Index the tuple by converting boolean values to int (0 or 1)
index = (not a) * 4 + (not b) * 2 + (not c) * 1
name = result[index]
