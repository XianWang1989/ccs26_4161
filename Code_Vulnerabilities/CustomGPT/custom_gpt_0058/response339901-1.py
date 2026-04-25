
try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)  # This will print: An error occurred: division by zero
else:
    print("No errors occurred, result is:", result)
finally:
    print("This will execute no matter what.")
