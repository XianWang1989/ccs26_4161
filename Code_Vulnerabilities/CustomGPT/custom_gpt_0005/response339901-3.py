
try:
    x = 1 / 0
except Exception as e:
    # Here e is already the caught exception
    print(f"An error occurred: {e}")
