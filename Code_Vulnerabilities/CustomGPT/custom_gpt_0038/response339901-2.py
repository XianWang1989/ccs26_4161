
try:
    # Code that may raise an exception
    number = int(input("Enter a number: "))
    result = 10 / number
except Exception:
    import sys
    e = sys.exc_info()[1]  # Getting the last exception
    print("An error occurred:", e)
