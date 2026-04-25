
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)  # Access the exception message
else:
    print("No errors, result is:", result)
finally:
    print("This block always executes.")
