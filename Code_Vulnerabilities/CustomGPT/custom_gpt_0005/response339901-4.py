
try:
    x = 1 / 0
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("This will not print since an error occurred.")
finally:
    print("Cleanup actions can be performed here.")
