
try:
    # Code that may raise an exception
    a = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    # Handling the exception
    print(f"An error occurred: {e}")
else:
    # Code that will run if no exception occurs
    print("No exceptions raised.")
finally:
    # Code that will run no matter what
    print("Execution complete.")
