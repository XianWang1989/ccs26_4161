
import sys

try:
    # Simulating an error
    x = 1 / 0
except Exception as e:
    # Handle the exception
    print(f"An error occurred: {e}")
else:
    # Code runs if no exception occurred
    print("No errors!")
finally:
    # This will always run
    print("Cleanup actions can be performed here.")
