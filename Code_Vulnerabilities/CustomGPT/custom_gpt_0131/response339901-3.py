
try:
    x = 1 / 0
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred. This executes if the try block is successful.")
finally:
    print("This will run no matter what.")  # This will execute even if there was an exception
