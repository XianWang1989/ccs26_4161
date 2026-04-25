
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)  # Prints: An error occurred: division by zero
else:
    print("No exceptions occurred, result is:", result)
finally:
    print("This will execute no matter what.")
