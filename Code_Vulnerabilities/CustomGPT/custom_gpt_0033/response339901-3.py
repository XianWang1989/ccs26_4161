
def risky_function():
    # Simulates a function that may raise an exception
    raise ValueError("An error occurred")

try:
    risky_function()
except Exception as e:
    print("Caught an exception:", e)  # e contains the exception details
else:
    print("No exceptions occurred!")
finally:
    print("This will always execute.")

# Output if an exception occurs:
# Caught an exception: An error occurred
# This will always execute.
