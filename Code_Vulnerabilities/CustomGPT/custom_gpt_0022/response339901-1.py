
try:
    # This will raise a ZeroDivisionError
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exceptions occurred! Result is:", result)
finally:
    print("This block always executes.")
