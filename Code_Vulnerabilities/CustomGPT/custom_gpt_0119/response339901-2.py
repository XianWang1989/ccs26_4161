
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception:
    e = "An error occurred"
    print(e)  # This will output the custom error message
