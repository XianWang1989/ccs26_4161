
try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("Caught an exception:", e)
else:
    print("No exceptions occurred.")
finally:
    print("Execution finished.")
