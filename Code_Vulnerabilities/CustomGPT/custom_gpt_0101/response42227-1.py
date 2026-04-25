
# Using tuple indexing to map boolean combinations to corresponding names
name = (
    'eighth',  # 0b000
    'seventh', # 0b001
    'sixth',   # 0b010
    'fifth',   # 0b011
    'fourth',  # 0b100
    'third',   # 0b101
    'second',  # 0b110
    'first'    # 0b111
)[(not a << 2) | (not b << 1) | (not c)]
