
try:
    # Some code that might raise an exception
    number = int(input("Enter an integer: "))
    result = 100 / number
except Exception:
    import sys
    e = sys.exc_info()[1]  # Get the exception information
    print("An error occurred:", e)
