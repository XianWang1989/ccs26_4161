
try:
    # Code that may cause an exception
    a = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)  # This prints: An error occurred: division by zero
else:
    print("No errors occurred!")
finally:
    print("This will always execute.")
