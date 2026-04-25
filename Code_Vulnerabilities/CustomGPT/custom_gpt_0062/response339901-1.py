
try:
    # Code that might raise an exception
    pass
except Exception:
    e = sys.exc_info()[1]  # Get the last exception raised
    print(e)  # You can now access the exception
