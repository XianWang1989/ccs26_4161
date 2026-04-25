
import sys

try:
    # Attempting to divide by zero to raise an exception
    result = 10 / 0
except Exception as e:
    # Print error message
    print("An error occurred:", e)
else:
    # This block runs if no exceptions were raised
    print("The result is:", result)
finally:
    # This block runs regardless of what happened above
    print("Execution completed.")
