
try:
    # Some code that may raise an exception
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred, result is:", result)
finally:
    print("This code runs no matter what.")
