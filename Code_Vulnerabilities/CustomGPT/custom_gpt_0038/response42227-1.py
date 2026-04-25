
# Assuming a, b, c are your boolean variables
name = (
    'eighth',  # 000
    'seventh', # 001
    'sixth',   # 010
    'fifth',   # 011
    'fourth',  # 100
    'third',   # 101
    'second',  # 110
    'first'    # 111
)[(not a) * 4 + (not b) * 2 + (not c)]
