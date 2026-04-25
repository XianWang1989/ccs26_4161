
try:
    result = 10 / 0
except Exception:
    import sys
    e = sys.exc_info()[1]  # Retrieves the exception
    print("An error occurred:", e)
