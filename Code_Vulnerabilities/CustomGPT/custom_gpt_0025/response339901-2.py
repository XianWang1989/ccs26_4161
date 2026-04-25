
try:
    result = 10 / 0
except Exception as e:
    error_message = str(e)  # Assign the error message to the variable
    print(f"An error occurred: {error_message}")
