
try:
    value = int(input("Enter a number: "))
    result = 10 / value  # Potential division by zero
except ValueError as e:
    print(f"Value error: {e}")
except ZeroDivisionError as e:
    print(f"Division error: {e}")
else:
    print("The result is:", result)
finally:
    print("Execution complete.")
