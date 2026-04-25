
try:
    result = 10 / 0  # This will raise an error
except Exception as e:
    print(f"An error occurred: {e}")  # Handle the exception
else:
    print("No exceptions occurred! Result is:", result)
finally:
    print("This block always executes, performing cleanup.")
