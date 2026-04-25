
try:
    result = 10 / 0
except Exception:
    # Create a new exception or capture message somehow
    e = "A generic error occurred."  # You can customize this message
    print(f"An error occurred: {e}")
else:
    print(f"The result is: {result}")
finally:
    print("Execution complete.")
