
name = (
    'eighth',  # (False, False, False)
    'seventh', # (False, False, True)
    'sixth',   # (False, True, False)
    'fifth',   # (False, True, True)
    'fourth',  # (True, False, False)
    'third',   # (True, False, True)
    'second',  # (True, True, False)
    'first'    # (True, True, True)
)[(not a) * 4 + (not b) * 2 + c]
