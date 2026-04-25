
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is: {result}")
finally:
    print("Execution complete.")
