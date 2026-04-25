
try:
    # Code that may raise an exception
    pass
except Exception as e:
    message = str(e)  # This captures the string representation of the error
else:
    # Execute if no exception occurs
    pass
finally:
    # Code that will always run, regardless of whether an exception occurred or not
    print("Execution completed.")  # This will run no matter what
