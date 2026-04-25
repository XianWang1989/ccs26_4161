
try:
    result = 10 / 0
except Exception:
    import sys
    e = sys.exc_info()[1]  # Gets the last exception caught
    print("An error occurred:", e)
