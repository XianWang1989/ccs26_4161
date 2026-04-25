
try:
    value = 10 / 0  # This will cause a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # 'e' contains the exception object
else:
    print("No errors occurred.")  # Executes if no exception is raised
finally:
    print("Execution completed.")  # Always executes, regardless of errors
