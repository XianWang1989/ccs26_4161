
try:
    # Some code that may raise an exception
    result = 10 / 0
except Exception:
    e = Exception("A specific error message")  # Manually creating an exception instance
    print(f"An error occurred: {e}")
