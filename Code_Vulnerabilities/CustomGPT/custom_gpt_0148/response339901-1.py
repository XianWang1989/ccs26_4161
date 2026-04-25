
try:
    # some code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(e)  # Prints: division by zero
