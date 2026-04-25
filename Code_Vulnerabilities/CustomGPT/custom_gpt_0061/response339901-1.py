
try:
    # Code that may raise an exception
    pass
except Exception as e:
    # This block executes if an exception occurs
    print(e)  # This prints the error message associated with the exception
else:
    # This block executes if no exceptions occur in the try block
    pass
finally:
    # This block always executes, whether or not an exception occurred
    pass
