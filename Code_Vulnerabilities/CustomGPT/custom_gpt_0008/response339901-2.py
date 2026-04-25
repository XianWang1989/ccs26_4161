
try:
    x = 1 / 0
except Exception:
    e = Exception("Custom error message")
    print(e)  # This will print: Custom error message
