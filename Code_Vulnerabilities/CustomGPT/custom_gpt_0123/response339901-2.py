
import sys

try:
    # Risky operation
    result = 10 / 0  # This will raise ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"No errors, result is: {result}")
finally:
    print("Execution complete. This runs no matter what.")
