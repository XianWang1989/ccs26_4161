
try:
    # Attempting a risky operation
    x = 1 / 0
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred.")
finally:
    print("Cleanup actions go here.")
