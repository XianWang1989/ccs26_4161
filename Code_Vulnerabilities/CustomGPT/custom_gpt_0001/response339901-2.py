
try:
    # Some code that might raise an exception
    result = 10 / 0
except Exception:
    e = Exception("A specific error occurred")  # Creating an exception manually
    print("An error occurred:", e)
else:
    print("The operation was successful:", result)
finally:
    print("This runs no matter what.")
