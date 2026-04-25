
try:
    # Simulating an error
    number = int(input("Enter a number: "))
    result = 100 / number  # This can raise ZeroDivisionError if number is 0
except Exception as e:
    print(f"An error occurred: {e}")  # Prints the error message
else:
    print("Result is:", result)  # Executed if no exception occurs
finally:
    print("Execution complete. Cleanup can be done here.")
