
try:
    # Code that may cause an exception
    result = 10 / 0
except Exception as e:
    print("An error occurred:", e)  # This prints the error message
else:
    print("No exceptions occurred, result is:", result)
finally:
    print("This block always executes.")
