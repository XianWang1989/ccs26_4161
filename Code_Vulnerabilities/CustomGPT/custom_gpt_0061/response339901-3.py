
try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)
else:
    print("Everything went fine!")
finally:
    print("This will always execute.")
