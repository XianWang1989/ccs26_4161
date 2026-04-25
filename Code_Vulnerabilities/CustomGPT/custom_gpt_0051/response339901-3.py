
try:
    # Potentially error-causing code
    x = int(input("Please enter a number: "))
    result = 10 / x
except ValueError as e:
    print(f"Value error occurred: {e}")
except ZeroDivisionError as e:
    print(f"Cannot divide by zero: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("The result is:", result)
finally:
    print("Execution completed.")
