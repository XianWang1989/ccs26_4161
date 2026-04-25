
try:
    # Intentional error
    result = 10 / 0
except Exception:
    e = Exception("Custom error message")
    print("An error occurred:", e)
finally:
    print("Cleanup actions go here.")
