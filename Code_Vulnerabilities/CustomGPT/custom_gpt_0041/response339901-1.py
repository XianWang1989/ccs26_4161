
try:
    # Sample code that may raise an exception
    x = 10 / 0
except Exception as e:
    print("An error occurred:", e)
else:
    print("No errors occurred.")
finally:
    print("This will always execute.")
