
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exceptions occurred, result is:", result)
finally:
    print("This will execute no matter what.")
