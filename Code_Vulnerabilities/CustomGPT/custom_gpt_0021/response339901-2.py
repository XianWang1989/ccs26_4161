
try:
    # code that may raise an exception
    pass
except Exception:
    import sys
    e = sys.exc_info()[1]  # Gets the exception instance
    print(e)
