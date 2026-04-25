
try:
    # This will raise a ZeroDivisionError
    result = 10 / 0
except Exception as e:
    print(f"Caught an exception: {e}")
else:
    print("No exceptions, result is:", result)
finally:
    print("This will run no matter what.")
