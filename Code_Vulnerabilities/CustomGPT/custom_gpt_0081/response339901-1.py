
try:
    # Code that may raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)
else:
    print("This runs if no exceptions occur.")
finally:
    print("This block always runs, regardless of whether an exception occurred.")
