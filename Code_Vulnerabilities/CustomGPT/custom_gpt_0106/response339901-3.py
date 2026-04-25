
try:
    x = 5 / 0
except Exception as e:
    print("Caught an exception:", e)
else:
    print("No exceptions, result:", x)
finally:
    print("Execution finished.")
