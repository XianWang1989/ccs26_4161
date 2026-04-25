
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)
else:
    print("Result:", result)
finally:
    print("Execution completed.")
