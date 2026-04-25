
try:
    # Code that may raise an exception
    pass
except Exception as e:
    # This block executes if an exception occurs
    print(e)  # Here, e contains the exception object
else:
    # This block executes if no exception occurs in the try block
    pass
finally:
    # This block always executes, regardless of whether an exception occurred or not
    pass
