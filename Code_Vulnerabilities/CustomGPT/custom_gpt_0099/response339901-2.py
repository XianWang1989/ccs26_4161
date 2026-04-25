
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception:
    import sys
    e = sys.exc_info()[1]  # Get the current exception
    print("An error occurred:", e)
