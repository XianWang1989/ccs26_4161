
try:
    # Code that may raise an exception
    pass
except Exception as e:
    # Code that handles the exception
    print(e)  # Here, e is the exception object
else:
    # Code that runs if no exceptions were raised
    pass
finally:
    # Code that runs no matter what (whether there was an exception or not)
    pass
