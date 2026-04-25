
try:
    result = 10 / 0
except Exception:
    e = "An error occurred."  # Here, you wouldn't get the actual exception details
    print(e)
