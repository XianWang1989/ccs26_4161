
try:
    # Code that may raise an exception
    pass
except Exception as e:
    # This block runs if an exception occurs
    print(e)  # e contains the exception instance
else:
    # This block runs if no exceptions are raised
    pass
finally:
    # This block runs no matter what, whether an exception occurred or not
    pass
