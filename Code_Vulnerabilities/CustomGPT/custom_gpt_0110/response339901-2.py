
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception:
    # Retrieve the last exception caught
    import sys
    e = sys.exc_info()[1]  # Retrieves the exception info
    print(f"An error occurred: {e}")
