
def risky_operation():
    return 1 / 0  # This will raise a ZeroDivisionError

try:
    risky_operation()
except Exception as e:
    print("Caught an exception:", e)  # Output the error message
else:
    print("Operation successful!")
finally:
    print("This always runs.")

# Output:
# Caught an exception: division by zero
# This always runs.
