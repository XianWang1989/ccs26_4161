
try:
    # code that may raise an exception
    x = 1 / 0
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred.")
finally:
    print("This will run no matter what.")
