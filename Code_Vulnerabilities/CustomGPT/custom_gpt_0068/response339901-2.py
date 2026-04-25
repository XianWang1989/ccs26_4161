
try:
    x = 1 / 0
except Exception:
    e = Exception("Custom error message")  # Simulating an exception
    print(f"An error occurred: {e}")

