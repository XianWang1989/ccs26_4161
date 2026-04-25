
try:
    # Some code that may raise an exception
    result = 10 / 0
except Exception:
    e = "An error occurred."  # You cannot retrieve the actual exception without 'as'
    print(e)
