
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception as e:
    print("An error occurred:", e)  # Outputs the error message
else:
    print("No errors, result is:", result)
finally:
    print("This block always executes.")
