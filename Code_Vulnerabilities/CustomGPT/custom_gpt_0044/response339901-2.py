
try:
    result = 10 / 0
except Exception:
    # Here, we create an exception instance manually
    e = Exception("A manual exception message")
    print("An error occurred:", e)
