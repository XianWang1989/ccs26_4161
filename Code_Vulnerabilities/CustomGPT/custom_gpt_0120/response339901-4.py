
try:
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)
else:
    print("No errors occurred.")
finally:
    print("This block always executes.")
