
try:
    # Simulating code that may raise an exception
    number = int(input("Enter a number: "))
    result = 10 / number
except Exception as e:
    print("An error occurred:", e)
else:
    print("Success! The result is:", result)
finally:
    print("Execution of the try-except block is complete.")
