
try:
    # Code that may raise an exception
    pass
except Exception as e:
    # Code that runs if an exception occurs
    print(e)  # Here, e contains the exception object
else:
    # Code that runs if no exception occurs
    pass
finally:
    # Code that always runs (regardless of exceptions)
    pass
