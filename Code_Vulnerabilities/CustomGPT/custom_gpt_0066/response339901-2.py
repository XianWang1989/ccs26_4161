
try:
    # Some risky code
    a = 1 / 0  # This will cause a ZeroDivisionError
except Exception:
    e = "An error occurred"
    print(e)  # This will print your custom error message
