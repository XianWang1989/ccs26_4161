
try:
    x = 1 / 0
except Exception:
    e = 'Caught an exception, but no details available.'
    print(e)
