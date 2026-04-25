
try:
    result = 10 / 0  # This will raise ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # e contains the exception info
else:
    print("No exceptions occurred.")
finally:
    print("Execution complete, cleaning up.")
