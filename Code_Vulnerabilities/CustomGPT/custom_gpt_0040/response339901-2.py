
try:
    # code that might cause an exception
    pass
except Exception:
    # Here we can instantiate the Exception class, but this doesn't capture the specific error.
    e = Exception("An error occurred")
    print(e)
