
try:
    # Some code
    raise ValueError("This is a custom error")
except Exception as e:
    print(e)
