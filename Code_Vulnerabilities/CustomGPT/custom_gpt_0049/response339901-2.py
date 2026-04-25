
try:
    result = 10 / 0
except Exception:
    e = Exception("A custom error message")  # This is not how exceptions are usually captured.
    print("An error occurred:", e)
