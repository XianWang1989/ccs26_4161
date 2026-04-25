
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception:
    # Capture the exception without assigning it to a variable
    e = "An error occurred"  # Simplified message
    print(e)
