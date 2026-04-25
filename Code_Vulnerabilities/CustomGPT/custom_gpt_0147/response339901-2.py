
try:
    value = 10 / 0  # This will raise a ZeroDivisionError
except Exception:  # Just catches the Exception
    e = "An error occurred."  # You might want to define a custom message instead
    print(e)  # This is an alternative way, but does not carry the exception details
