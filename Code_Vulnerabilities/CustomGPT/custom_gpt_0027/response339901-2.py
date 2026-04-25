
try:
    result = 10 / 0
except Exception:
    e = Exception("Custom error message")  # Create a new Exception instance
    print(f"An error occurred: {e}")
