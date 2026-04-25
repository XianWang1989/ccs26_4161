
try:
    # Intentional error (division by zero)
    result = 10 / 0
except Exception as e:
    print("An error occurred:", e)
else:
    print("Result is:", result)
finally:
    print("This will run no matter what.")
