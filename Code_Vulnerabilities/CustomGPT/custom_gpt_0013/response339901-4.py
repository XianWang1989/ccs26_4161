
try:
    # Intentional error (division by zero)
    result = 10 / 0
except Exception as e:
    print(f"Caught an exception: {e}")
else:
    print("No exceptions occurred, result is:", result)
finally:
    print("Execution complete.")
