
try:
    # Potentially problematic code
    x = 1 / 0
except Exception as e:
    # Handle the exception and output the error message
    print(f"An error occurred: {e}")  
else:
    # This runs if no exceptions occurred
    print("No errors occurred.")
finally:
    # This runs no matter what
    print("Cleanup or final actions go here.")
