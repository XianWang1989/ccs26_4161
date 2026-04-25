
try:
    # Some code that might raise an exception
    result = 10 / 0
except Exception as e:
    print("An error occurred:", e)
else:
    print("The operation was successful:", result)
finally:
    print("This runs no matter what.")
