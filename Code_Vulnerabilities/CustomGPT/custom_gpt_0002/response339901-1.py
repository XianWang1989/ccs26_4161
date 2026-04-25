
try:
    # Some code that may raise an exception
    pass
except Exception as e:
    print(e)  # Print the error message
else:
    # Code to execute if no exceptions were raised
    pass
finally:
    # This block always executes, regardless of whether an exception occurred
    print("This will always execute.")
