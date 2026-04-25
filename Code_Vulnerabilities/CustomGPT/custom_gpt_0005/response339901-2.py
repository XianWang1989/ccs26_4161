
try:
    x = 1 / 0
except Exception:
    # Manually creating the exception object
    e = Exception("Manual exception")
    print(f"An error occurred: {e}")
